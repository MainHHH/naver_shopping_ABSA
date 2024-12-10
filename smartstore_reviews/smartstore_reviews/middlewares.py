# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter



class SmartstoreReviewsSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class SmartstoreReviewsDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


# SeleniumWireMiddleware


# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

class NavershoppingDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn't have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class navershoppingDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)



# SeleniumWireMiddleware
import gzip
import json
from scrapy.http import HtmlResponse
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from scrapy.signalmanager import dispatcher


class SeleniumMiddleware:
    def __init__(self, *args, **kwargs):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')  # Uncomment for headless mode
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.header_overrides = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
        }

        dispatcher.connect(self.spider_closed, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_request(self, request, spider):
        # smartstore crawling part
        if 'use_selenium_smartstore' in request.meta:
            self.driver.get(request.url)

            # Wait for the main body or a specific element to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )

            # Extract and navigate through paginated content
            page_number = 1  # Starting page number
            all_reviews = []  # To store all extracted reviews

            # Scroll to load dynamic content
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            self.driver.execute_script(f"window.scrollTo(0, {last_height * 2 / 3});")
            time.sleep(2)

            # Wait for a specific section to ensure content is loaded
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'REVIEW'))
            )

            while True:
                try:
                    # Click the next page button if available
                    next_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, f"//a[@class='UWN4IvaQza _nlog_click' and text()='{page_number + 1}']")
                        )
                    )
                    next_button.click()
                    spider.logger.info(f"Moved to page {page_number + 1}")
                    page_number += 1
                    time.sleep(5)

                except Exception as e:
                    spider.logger.info(f"No more pages or an error occurred: {e}")
                    break

            # Capture POST requests and process responses
            for request_ in self.driver.requests:
                if request_.method == 'POST' and 'i/v1/contents/reviews/query-pages' in request_.url:
                    if request_.response:
                        try:
                            compressed_data = request_.response.body
                            decompressed_data = gzip.decompress(compressed_data)
                            json_data = json.loads(decompressed_data.decode('utf-8'))

                            for review in json_data['contents']:
                                all_reviews.append(review)

                        except Exception as e:
                            spider.logger.error(f"Failed to process response data: {e}")

            # self.driver.quit()

            # Combine all reviews into a single HTML response for the spider
            return HtmlResponse(
                url=self.driver.current_url,
                body=json.dumps({'contents': all_reviews}, ensure_ascii=False).encode('utf-8'),
                encoding='utf-8',
                request=request
            )

        # brand crawling part
        if 'use_selenium_brand' in request.meta:
            self.driver.get(request.url)

            # Wait for the main body or a specific element to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'body'))
            )

            # Extract and navigate through paginated content
            page_number = 1  # Starting page number
            all_reviews = []  # To store all extracted reviews

            # Scroll to load dynamic content
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            self.driver.execute_script(f"window.scrollTo(0, {last_height * 2 / 3});")
            time.sleep(2)

            # Wait for a specific section to ensure content is loaded
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'REVIEW'))
            )

            while True:
                try:
                    # Click the next page button if available
                    next_page_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                            (By.XPATH, f"//a[@class='UWN4IvaQza _nlog_click' and text()='{page_number + 1}']")
                        )
                    )
                    next_page_button.click()
                    spider.logger.info(f"Moved to page {page_number + 1}")
                    page_number += 1
                    time.sleep(5)

                except:
                    try:
                        next_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable(
                                (By.XPATH, '//*[@class="fAUKm1ewwo _2Ar8-aEUTq _nlog_click"]')
                            )
                        )
                        next_button.click()
                        time.sleep(5)
                    except Exception as e:
                        spider.logger.info(f"No more pages or an error occurred: {e}")
                        break

            # Capture POST requests and process responses
            for request_ in self.driver.requests:
                if request_.method == 'POST' and 'n/v1/contents/reviews/query-pages' in request_.url:
                    if request_.response:
                        try:
                            compressed_data = request_.response.body
                            decompressed_data = gzip.decompress(compressed_data)
                            json_data = json.loads(decompressed_data.decode('utf-8'))

                            for review in json_data['contents']:
                                all_reviews.append(review)

                        except Exception as e:
                            spider.logger.error(f"Failed to process response data: {e}")

            # self.driver.quit()

            # Combine all reviews into a single HTML response for the spider
            return HtmlResponse(
                url=self.driver.current_url,
                body=json.dumps({'contents': all_reviews}, ensure_ascii=False).encode('utf-8'),
                encoding='utf-8',
                request=request
            )

        return None

    def spider_closed(self, spider):
        print("="*100)
        if self.driver:
            self.driver.quit()
