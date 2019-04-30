#!/usr/bin/env python3
# 我们知道利用urlopen()方法可以实现最基本的请求发起，但这几个简单的参数并不足以构建一个完整的请求。如果请求中需要加入Headers等信息，就可以利用更强大的Request类构建。通过构造这个数据结构，一方面我们可以将请求独立成一个对象，另一方面可以更加丰富灵活地配置参数。
# class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
# 第一个参数url用于请求URL，这是必传参数，其他都是可选参数。
# 第二个参数data如果要传，必须传bytes(字节流)类型的。如果它是字典，可以先用urllib.parse模块里的urlencode()编码。
# 第三个参数headers是一个字典，它是请求头，我们可以在构造请求时通过headers参数直接构造，也可以通过调用请求实例的add_header()方法添加。
# 添加请求头最常用的用法就是通过修改User-Agent来伪装浏览器，默认的User-Agent是Python-urllib，我们可以通过修改它来伪装浏览器。
# 第四个参数origin_req_host指的是请求方的host名称或者IP地址。
# 第五个参数unverifiable表示这个请求是否是无法验证的，默认是False，意思就是说用户没有足够权限来选择接收这个请求的结果。例如，我们请求一个HTML文档中的图片，但是我们没有向动抓取图像的权限，这时unverifiable的值就是True。
# 第六个参数method是一个字符串，用来指示请求使用的方法，比如GET、POST和PUT等。
from urllib import request, parse
url = 'http://httpbin.org/post'
headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host': 'httpbin.org'
        }
data = {
        'name': 'Germey'
        }
data = bytes(parse.urlencode(data), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
# 观察结果可以发现我们成功设置了data、headers和method。
# 另外，headers也可以用add_header()方法来添加。
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
