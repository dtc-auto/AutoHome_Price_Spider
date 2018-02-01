# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChexunSpiderPriceItem(scrapy.Item):
    appversion = scrapy.Field()
    spec_name = scrapy.Field()
    mileage = scrapy.Field()
    reg_date = scrapy.Field()
    price = scrapy.Field()
    grade = scrapy.Field()
    q0 = scrapy.Field()
    q1 = scrapy.Field()
    q2 = scrapy.Field()
    q3 = scrapy.Field()
    q4 = scrapy.Field()
