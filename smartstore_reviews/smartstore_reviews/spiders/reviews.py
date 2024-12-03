import scrapy


class ReviewsSpider(scrapy.Spider):
    name = "reviews"
    allowed_domains = ["smartstore.naver.com"]

    def start_requests(self):
        start_urls = "https://smartstore.naver.com/i/v1/contents/reviews/query-pages"
        formdata = {
            "checkoutMerchantNo": "500235951",
            "originProductNo": "4729223012",
            "page": "1",
            "pageSize": "20",
            "reviewSearchSortType": "REVIEW_RANKING"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }

        yield scrapy.FormRequest(
            url=start_urls,
            callback=self.parse,
            formdata=formdata,
            method='POST',
            headers=headers,
        )

    def parse(self, response):
        return response