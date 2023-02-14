import scrapy

from crawl.items import PottchangeItem


class PottchangeSpider(scrapy.Spider):
    name = 'PottchangeSpider'
    start_urls = ['https://www.pottchange.com/wisselkoersen/']

    def parse(self, response):
        rates = response.css('.pott-tr-odd') + response.css('.pott-tr-even')
        for rate in rates:
            result = {
                "land_code": rate.css('.pott-td-short::text').get(),
                "sell_per_100": rate.css('.pott-td-buy::text').get(),
                "buy_per_100": rate.css('.pott-td-sell::text').get(),
                "sell_per_euro": rate.css('.pott-td-buy::text').get(),
                "buy_per_euro": rate.css('.pott-td-sell::text').get(),
            }
            yield PottchangeItem(**result)
