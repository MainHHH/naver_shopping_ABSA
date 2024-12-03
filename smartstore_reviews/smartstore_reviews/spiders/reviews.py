import scrapy


class ReviewsSpider(scrapy.Spider):
    name = "reviews"
    allowed_domains = ["smartstore.naver.com"]
    start_urls = ["https://smartstore.naver.com/i/v1/contents/reviews/query-pages"]

    def parse(self, response):

        pass
