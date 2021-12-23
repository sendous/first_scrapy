import scrapy
from scrapy.loader import ItemLoader
from ..items import DeadCoins
from first_scrapy.items import Article, DeadCoins, Coins


class firstSpider(scrapy.Spider):
    name = "deadcoins"
    allowed_domains = ["99bitcoins.com"]
    start_urls = ["https://99bitcoins.com/deadcoins/"]

    # def parse(self, response):
    #     for href in response.css(".w3-clear.nextprev > a::attr('href')"):
    #         url = response.urljoin(href.extract())
    #         yield scrapy.Request(url, callback=self.parse_dir_contents)

    # def parse_dir_contents(self, response):
    #     for article in response.xpath("//div"):
    #         item = W3Schools()
    #         item['title'] = article.xpath('a/text()').extract()
    #         item['link'] = article.xpath('a/@href').extract()
    #         item['desc'] = article.xpath('text()').extract()
    #         yield item

    # Extract article information
    # def extract_css_article_parse(self, response, **kwargs):
    #
    #     for title in response.xpath("/html"):
    #         item = Article()
    #         item['title'] = title.xpath("//title/text()").extract()
    #         item['subtitle'] = title.xpath("//div[@id='main']/h2/text()").extract()
    #         yield item
    #
    #     next_page = response.css(".w3-clear.nextprev > a.w3-right.w3-btn::attr('href')")
    #     if next_page:
    #         url = response.urljoin(next_page[0].extract())
    #         yield scrapy.Request(url, self.parse)

    def parse(self, response, **kwargs):
        for deadcoins in response.css(".list > tr"):
            loader = ItemLoader(item=DeadCoins(), selector=deadcoins)
            loader.add_css('name', 'td.nnbitcoins-deadcoins-list-item-name::text')
            loader.add_css('ticker', 'td.nnbitcoins-deadcoins-list-item-ticker::text,\
                                        td.nnbitcoins-deadcoins-list-item-ticker > *::text')
            loader.add_css('death_indicators', 'td.nnbitcoins-deadcoins-list-item-death-indicators > ul > li > a::text')
            yield loader.load_item()



        # next_page = response.css("#example_paginate > a#example_next::attr('href')")
        # if next_page:
        #     url = response.urljoin(next_page[0].extract())
        #     yield scrapy.Request(url, self.parse)


class coin(scrapy.Spider):
    name = "coin"
    allowed_domains = ["coinmarketcap.com"]
    start_urls = ["https://coinmarketcap.com/"]

    def parse(self, response, **kwargs):
        for coins in response.xpath("//table/tr"):
            item = Coins()
            item['name'] = coins.xpath("//td[3]/div/a/div/div/p/text()").extract()
            yield item
