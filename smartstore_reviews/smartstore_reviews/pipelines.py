# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
import re
import csv

class SmartstoreReviewsPipeline:
    def open_spider(self, spider):
        # 스파이더가 시작될 때 CSV 파일 열기
        self.file = open('crawling_data.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, fieldnames=['smartstore', 'product_name', 'product_id', 'product_option', 'user_id', 'apply_date', 'review', 'stars_score', 'thumb_count'])
        self.writer.writeheader()

    def process_item(self, item, spider):
        # 리뷰 전처리
        item['review'] = self.clean_emoji(item.get('review'))
        # 옵션 전처리
        item['product_option'] = self.clean_emoji(item.get('product_option'))
        # 상품 이름 전처리
        item['product_name'] = self.clean_emoji(item.get('product_name'))
        # 날짜 전처리
        item['apply_date'] = self.format_datetime(item.get('apply_date'))

        # CSV 파일에 저장
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        # 스파이더가 종료될 때 파일 닫기
        self.file.close()

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