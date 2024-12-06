import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import json
import argparse

class navershopping(scrapy.Spider):
    name = "navershopping"

    def __init__(self, brand=None, product_no=None, *args, **kwargs):
        super(navershopping, self).__init__(*args, **kwargs)
        self.brand = brand
        self.product_no = product_no

    def start_requests(self):
        if self.brand and self.product_no:
            url = f'https://smartstore.naver.com/{self.brand}/products/{self.product_no}'
            yield scrapy.Request(url=url, meta={'use_selenium': True})
        else:
            self.logger.error("Brand or product number not provided.")

    def parse(self, response):
        self.logger.info(f'Response received from {response.url}')
        try:
            data = json.loads(response.text)
            for item in data['contents']:
                yield {
                    'reviewContent': item['reviewContent'],
                    'writerId': item['writerId'],
                    'productNo': item['productNo'],
                    'productOptionContent': item['productOptionContent'],
                    'reviewScore': item['reviewScore'],
                    'createDate': item['createDate'],
                }
        except json.JSONDecodeError:
            self.logger.error("Failed to decode JSON from response.")

#  debug setting
if __name__ == "__main__":
    # Command line argument parsing
    parser = argparse.ArgumentParser(description="Run Naver Shopping Scraper")
    parser.add_argument("--brand", required=True, help="Brand name for the Naver shopping URL")
    parser.add_argument("--product_no", required=True, help="Product number for the Naver shopping URL")
    args = parser.parse_args()

    settings = get_project_settings()
    settings["LOG_LEVEL"] = "DEBUG"
    process = CrawlerProcess(settings=settings)

    # Pass arguments to the spider
    process.crawl(navershopping, brand=args.brand, product_no=args.product_no)
    process.start()
