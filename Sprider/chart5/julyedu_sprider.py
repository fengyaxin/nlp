import scrapy


class JulyeduSprider(scrapy.Spider):
    name = 'julyedu'
    start_urls = ['https://www.julyedu.com/category/index']

    def parse(self, response):
        for julyedu_class in response.xpath('//*[@id="course"]/div[1]/div[1]/div[7]/a'):
            print(julyedu_class.xpath('div[@class="course-title"]/text()'))

            yield {'title': julyedu_class.xpath('div[@class="course-title"]/text()')}
