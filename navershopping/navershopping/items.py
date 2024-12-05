# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NavershoppingItem(scrapy.Item):
    # define the fields for your item here like:
    reviewContent = scrapy.Field()

    writerId=scrapy.Field()

    productNo=scrapy.Field()

    productOptionContent=scrapy.Field()

    reviewScore=scrapy.Field()

    createDate=scrapy.Field()
    pass
