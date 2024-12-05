import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import json

class navershopping(scrapy.Spider):
    name = "navershopping"
    start_urls = ['https://smartstore.naver.com/lottesuw31/products/10986057309']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, meta={'use_selenium': True})

    def parse(self, response):
        self.logger.info(f'Response received from {response.url}')
        data=json.loads(response.text)
        for item in data['contents']:
            yield {
                'reviewContent':item['reviewContent'],
                'writerId':item['writerId'],
                'productNo':item['productNo'],
                'productOptionContent':item['productOptionContent'],
                'reviewScore':item['reviewScore'],
                'createDate':item['createDate'],
            }

#  vscode의 파이썬 Extension으로 디버깅을 하기 위한 세팅입니다.
if __name__ == "__main__":
    settings = get_project_settings()
    settings["LOG_LEVEL"] = "DEBUG"
    process = CrawlerProcess(settings=settings)
    process.crawl(navershopping)
    process.start()