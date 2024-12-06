import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from smartstore_reviews.items import SmartstoreReviewsItem
import json
import argparse

class navershopping(scrapy.Spider):
    name = "navershopping"

    def __init__(self, where=None, brand=None, product_no=None, *args, **kwargs):
        super(navershopping, self).__init__(*args, **kwargs)
        self.brand = brand
        self.product_no = product_no
        self.where = where

    def start_requests(self):
        if self.where == "smartstore" and self.brand and self.product_no:
            url = f'https://smartstore.naver.com/{self.brand}/products/{self.product_no}'
            yield scrapy.Request(url=url, meta={'use_selenium_smartstore': True})
        elif self.where == "brand" and self.brand and self.product_no:
            url = f'https://brand.naver.com/{self.brand}/products/{self.product_no}'
            yield scrapy.Request(url=url, meta={'use_selenium_brand': True})
        else:
            self.logger.error("Brand or product number not provided.")

    def parse(self, response):
        self.logger.info(f'Response received from {response.url}')
        item = SmartstoreReviewsItem()
        try:
            data = json.loads(response.text)
            for content in data['contents']:
                item['smartstore'] = self.brand
                item['product_name'] = content['productName']
                item['product_id'] = content['productNo']
                item['product_option'] = content['productOptionContent']
                item['user_id'] = content['writerId']
                item['apply_data'] = content['createDate']
                item['review'] = content['reviewContent']
                item['stars_score'] = content['reviewScore']
                item['thumb_count'] = content['helpCount']
                yield item
        except json.JSONDecodeError:
            self.logger.error("Failed to decode JSON from response.")

#  debug setting
if __name__ == "__main__":
    # Command line argument parsing
    parser = argparse.ArgumentParser(description="Run Naver Shopping Scraper")
    parser.add_argument("--where", required=True, help="smartstore or brand")
    parser.add_argument("--brand", required=True, help="Brand name for the Naver shopping URL")
    parser.add_argument("--product_no", required=True, help="Product number for the Naver shopping URL")
    args = parser.parse_args()

    settings = get_project_settings()
    settings["LOG_LEVEL"] = "DEBUG"
    process = CrawlerProcess(settings=settings)

    # Pass arguments to the spider
    process.crawl(navershopping, brand=args.brand, product_no=args.product_no)
    process.start()