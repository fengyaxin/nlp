import time
from selenium import webdriver

'''
第3讲 爬虫实例---自己整理版
'''

browser = webdriver.Chrome()
browser.set_page_load_timeout(30)

# get 方法  打开指定网址
browser.get('http://www.17huo.com/search.html?sq=2&keyword=%E7%BE%8A%E6%AF%9B')

# 选择网页元素
page_info = browser.find_element_by_css_selector('body > div.wrap > div.pagem.product_list_pager > div')

# print(page_info.text)   #共 80 页，每页 24 条

# 获取页码（80）
pages = page_info.text.split(' ')[1]    # pages=80

# 例：range(3)=[0,1,2]
for page in range(int(pages)):
    print(page)
    if page > 2:
        break
    # 拼接获取每一页的地址
    url = 'http://www.17huo.com/?mod=search&sq=2&keyword=%E7%BE%8A%E6%AF%9B&page=' + str(page + 1)

    browser.get(url)
    # 滚动到底部(因图片是滚动后才会加载)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)   # 不然会load不完整
    goods = browser.find_element_by_css_selector('body > div.wrap > div:nth-child(2) > div.p_main > ul').find_elements_by_tag_name('li')

   # print('d%页有%d个商品' % ((page + 1), len(goods)))

    for good in goods:
        try:
            title = good.find_element_by_css_selector('a:nth-child(1) > p:nth-child(2)')
            price = good.find_element_by_css_selector('div > a > span')
            print(title, price)
        except:
            print(good.text)
