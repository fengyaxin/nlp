from bs4 import BeautifulSoup

soup = BeautifulSoup(open('test.html'))
#BeautifulSoup的格式化输出函数--prettify()
#print(soup.prettify())

# Tag
'''
print(type(soup.title))   
print(soup.title.name)
print(soup.title)   # <title>The Dormouse's story</title>
'''

# string
'''
print(type(soup.title.string))  #<class 'bs4.element.NavigableString'>
print(soup.title.string)   # The Dormouse's story
'''

# 注释
'''
print(type(soup.a.string))  # <class 'bs4.element.Comment'>
print(soup.a.string)  # Elsie 
'''


'''
for item in soup.body.contents:
    print(item.name)
'''


#CSS查询
'''
print(soup.select('.sister'))
print(soup.select('#link1'))
print(soup.select('head > title'))
'''

a_s = soup.select('a')
for a in a_s:
    print(a)
