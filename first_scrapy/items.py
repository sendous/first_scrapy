# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DeadCoins(scrapy.Item):
    name = scrapy.Field()
    ticker = scrapy.Field()
    death_indicators = scrapy.Field()


class Article(scrapy.Item):
    title = scrapy.Field()
    subtitle = scrapy.Field()


class Coins(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    volume = scrapy.Field()
    mkt_cap = scrapy.Field()
