#!/usr/bin/env python3
# data参数是可选的。如果要添加该参数，并且如果它是字节流编码格式的内容，即bytes类型，则需要通过bytes()方法转化。另外，如果传递了这个参数，则它的请求就不再是GET方式，而是POST方式。
import urllib.request, urllib.parse, socket, urllib.error
data = bytes(urllib.parse.urlencode({'gaSearch': 'rs1045642', 'query': 'rs1045642'}), encoding='utf8')
response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
print(response.read().decode('utf-8'))
# 这里我们传递了两个参数，它需要被转码成bytes(字节流)类型。其中转字节流采用了bytes()方法，该方法的第一个参数需要是str(字符串)类型，需要用urllib.parse模型块里的urlencode()方法来将参数字典转化为字符串；第二个参数指定编码格式，这里指定为utf8。这里请求的站点是httpbin.org，它可以提供HTTP请求测试。本次请求为URL http://httpbin.org/post，这个链接可以用来测试POST请求，它可以输出请求的一些信息，其中包含我们传递的data参数。

# timeout参数
# 用于设置超时时间，单位为秒，如果请求超出了设置的这个时间，还没有得到响应，就会抛出异常。如果不指定该参数，就会使用全局默认时间。它支持http、https、ftp等请求。我们可以设置超时时间来控制一个网页如果长时间未响应，就跳过它的抓取。可以通过try except语句来实现。

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

# 这里我们请求了http://httpbin.org/get测试链接，设置超时时间是0.1秒，然后捕获了URLError异常，接着判断异常是socket.timeout类型（意思就是超时异常），从而得出它确实是因为超时而报错，打印输出了TIMEOUT。
