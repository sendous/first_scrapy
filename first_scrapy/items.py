# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join, Identity, Compose
from w3lib.html import remove_tags


def replace_and_sign(value):
    inactive_development = value.replace("Inactive Development", "توسعه غیرفعال").\
        replace("Inactive Twitter", "توئیتر غیرفعال").\
        replace("Low Volume", "حجم پایین").\
        replace("Not indexed", "جایی لیست نشده").\
        replace("Not Listed on exchanges", "در هیچ صرافی لیست نشده").\
        replace("Website Down", "آفلاین بودن سایت")
    return inactive_development


class DeadCoins(scrapy.Item):
    name = scrapy.Field()
    ticker = scrapy.Field()
    death_indicators = scrapy.Field(input_processor=MapCompose(
        remove_tags, replace_and_sign), output_processor=Identity())


class Article(scrapy.Item):
    title = scrapy.Field()
    subtitle = scrapy.Field()


class Coins(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    volume = scrapy.Field()
    mkt_cap = scrapy.Field()
