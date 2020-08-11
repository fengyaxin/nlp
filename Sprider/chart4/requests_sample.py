import requests
import json
from PIL import Image
from io import BytesIO

# 查看requests有哪些方法
# print(dir(requests))

'''
# 1
url = 'http://www.baidu.com'
r = requests.get(url)
print(r.status_code)
print(r.encoding)
print(r.text)
'''


'''
# 2、传递参数:比如  http://aaa.com?xx=dd&yy=cc

# httpbin.org 这个网站能测试 HTTP 请求和响应的各种信息，
# 比如 cookie、ip、headers 和登录验证等，且支持 GET、POST 等多种方法，对 web 开发和测试很有帮助

params = {'k1': 'v1', 'k2': [1, 2, 3]}
params2 = {'k1': 'v1', 'k2': None}
r = requests.get('http://httpbin.org/get', params)
r2 = requests.get('http://httpbin.org/get', params2)

print(r.url)   # http://httpbin.org/get?k1=v1&k2=1&k2=2&k2=3
print(r2.url)  # http://httpbin.org/get?k1=v1
'''

'''
# 3、二进制
# 图片做为二进制数据进行处理，获取图片的地址，然后通过二进制转换为图片并存储下来
r = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596882215745&di=9fc507f730a89109c55400b455c604bd&imgtype=0&src=http%3A%2F%2Fp2.so.qhimgs1.com%2Ft01dfcbc38578dac4c2.jpg')
image = Image.open(BytesIO(r.content))
image.save('picture.jpg')
'''

'''
# 4、json处理
r = requests.get('https://github.com/timeline.json')
print(type(r.json()))
# print(r.json())
print(r.text)
'''

'''
# 5、原始数据处理
# 以流数据存储一张照片
r = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596882215745&di=9fc507f730a89109c55400b455c604bd&imgtype=0&src=http%3A%2F%2Fp2.so.qhimgs1.com%2Ft01dfcbc38578dac4c2.jpg', stream = True)
with open('picture2.jpg', 'wb+') as f:
    for chunk in r.iter_content(1024):
        f.write(chunk)
'''

# # 6、提交表单
# form = {'username': 'user', 'password': 'pass'}
# r = requests.post('http://httpbin.org/post', data=form)
# print(r.text)    # form表单形式
# r = requests.post('http://httpbin.org/post', data=json.dumps(form))
# print(r.text)   # data形式


'''
# 7、cookie   
url = 'http://www.baidu.com'
r = requests.get(url)
#字典对象
cookies = r.cookies
#遍历字典对象
for k, v in cookies.get_dict().items():
    print(k, v)
'''

'''
cookies = {'c1': 'v1'}
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(r.text)
'''

# 8、重定向和重定向历史
r = requests.head('http://github.com', allow_redirects = True)
print(r.url)
print(r.status_code)
print(r.history)

'''
# 9、代理(示例)
proxies = {'http': '...', 'https': '...'}
r = requests.get('...', proxies = proxies)
'''