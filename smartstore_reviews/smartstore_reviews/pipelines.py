# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import re
from scrapy.exceptions import DropItem
from datetime import datetime

class SmartstoreReviewsPipeline:
    def open_spider(self, spider):
        """스파이더가 열릴 때 DB 연결"""
        self.conn = pymysql.connect(
            host=spider.settings.get('MYSQL_HOST'),
            user=spider.settings.get('MYSQL_USER'),
            password=spider.settings.get('MYSQL_PASSWORD'),
            database=spider.settings.get('MYSQL_DATABASE'),
            port=spider.settings.get('MYSQL_PORT'),
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        """스파이더가 닫힐 때 DB 연결 종료"""
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        """데이터를 DB에 삽입"""
        # 리뷰 전처리
        item['review'] = self.clean_emoji(item.get('review'))
        # 옵션 전처리
        item['product_option'] = self.clean_emoji(item.get('product_option'))
        # 상품 이름 전처리
        item['product_name'] = self.clean_emoji(item.get('product_name'))
        # 날짜 전처리
        item['apply_date'] = self.format_datetime(item.get('apply_date'))

        try:
            query = f"""
                    INSERT INTO reviews (smartstore, product_name, product_id, product_option, user_id, apply_date, review, stars_score, thumb_count)
                    SELECT '{item.get('smartstore')}', '{item.get('product_name')}', '{item.get('product_id')}', '{item.get('product_option')}', '{item.get('user_id')}', '{item.get('apply_date')}', '{item.get('review')}', '{item.get('stars_score')}', '{item.get('thumb_count')}'
                    WHERE NOT EXISTS (
                        SELECT 1
                        FROM reviews
                        WHERE product_id = '{item.get('product_id')}'
                          AND product_option = '{item.get('product_option')}'
                          AND user_id = '{item.get('user_id')}'
                          AND apply_date = '{item.get('apply_date')}'
                    );
                    """

            self.cursor.execute(query)

            return item
        except Exception as e:
            spider.logger.error(f"Error inserting item: {e}")
            raise DropItem(f"Failed to insert item: {item}")

    def clean_emoji(self, review):
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # 감정 표현 이모티콘
            "\U0001F300-\U0001F5FF"  # 기호 및 객체
            "\U0001F680-\U0001F6FF"  # 교통 및 기계
            "\U0001F700-\U0001F77F"  # 기타 기호
            "\U0001F780-\U0001F7FF"  # 추가적인 기호
            "\U0001F800-\U0001F8FF"  # 기호 확장
            "\U0001F900-\U0001F9FF"  # 이모티콘 확장
            "\U0001FA00-\U0001FA6F"  # 추가 기호
            "\U0001FA70-\U0001FAFF"  # 기타 범위
            "\u2600-\u26FF"  # 기타 기호
            "\u2700-\u27BF"  # 딩뱃
            "]",
            flags=re.UNICODE
        )
        if review:
            # 이모티콘 제거
            review = emoji_pattern.sub("", review)
            # 줄바꿈 문자 제거
            review = re.sub(r'\n', ' ', review)
            # 추가 공백 제거
            review = re.sub(r'\s+', ' ', review).strip()

            return review

    def format_datetime(self, apply_date):
        """날짜를 MySQL DATETIME 형식으로 변환"""
        if apply_date:
            try:
                # 문자열을 파싱하여 datetime 객체로 변환
                dt = datetime.strptime(apply_date, "%Y-%m-%dT%H:%M:%S.%f%z")
                # MySQL DATETIME 형식으로 변환
                return dt.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError as e:
                print(e)
        return None