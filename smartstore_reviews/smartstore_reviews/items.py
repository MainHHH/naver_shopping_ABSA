# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmartstoreReviewsItem(scrapy.Item):
    # 스토어 이름
    smartstore = scrapy.Field()
    # 상품 이름
    product_name = scrapy.Field()
    # 상품 번호
    product_id = scrapy.Field()
    # 상품 옵션
    product_option = scrapy.Field()
    # 고객 id
    user_id = scrapy.Field()
    # 등록 일자
    apply_data = scrapy.Field()
    # 내용
    review =scrapy.Field()
    # 별점
    stars_score = scrapy.Field()
    # 도움이 됬어요 갯수
    thumb_count = scrapy.Field()