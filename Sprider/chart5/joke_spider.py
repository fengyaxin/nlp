'''
第3种方式：解析内容的同时，返回下一页的链接并爬取
'''

import scrapy

class JokeSpider(scrapy.Spider):
    name = 'JokeSoider'
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    def parse(self, response):
        for joke in response.xpath('div[@class="quote"]'):
            print(joke.xpath('span[1]/text()')).extract_first()
            print(joke.xpath('span[2]/small/text()')).extract_first()

        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
