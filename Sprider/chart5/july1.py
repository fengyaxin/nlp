import scrapy

'''
场景一：爬取一页内容

待调试
'''

class july1(scrapy.Spider):
    name = 'july'
    start_urls = ['http://www.arkai.net/sysConfigItem/showList']

    def parse(self, response):
        print("1111111111111111111")
        print(response.xpath('//div'))
        print(response.xpath('//div[@class="class-list classfind-list"]/ul/li'))
        for july_class in response.xpath('//div[@class="class-list classfind-list"]/ul/li'):
            print(july_class)
            print(july_class.xpath('div/div[2]/div[@class="stageMove"]/p/text()').extract_first())

            yield {'author': july_class.xpath('div/div[2]/div[@class="stageMove"]/p/text()').extract_first()}


