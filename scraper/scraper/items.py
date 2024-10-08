# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    date = scrapy.Field()
    breakfast = scrapy.Field()
    lunch = scrapy.Field()
    dinner = scrapy.Field()
