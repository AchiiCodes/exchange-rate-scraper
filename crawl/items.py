import scrapy


class PottchangeItem(scrapy.Item):
    """ Definition of the PottchangeItem """

    land_code = scrapy.Field()
    sell_per_100 = scrapy.Field()
    buy_per_100 = scrapy.Field()
    sell_per_euro = scrapy.Field()
    buy_per_euro = scrapy.Field()