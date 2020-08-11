import scrapy
'''
场景二：
可以拼接出URL
例如：博客园精选
https://www.cnblogs.com/pick/#p3
'''


class cnblog(scrapy.Spider):
    name = 'cnblog'
    start_urls = ['https://www.cnblogs.com/pick/#p%s' % p for p in range(1, 2)]

    def parse(self, response):
        for blog in response.xpath('//div[@class="post-list"]/article'):
            print(blog.xpath('section/div/a/text()').extract_first())

            yield {'author': blog.xpath('section/div/a/text()').extract_first()}

