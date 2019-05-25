#!/usr/bin/env python3
# 发送请求后，得到的自然就是响应。在之前的实例中，我们使用text和content获取了响应的内容。此外还有很多属性和方法可以用来获取其他信息，比如状态码、响应头、Cookies等。
import requests
r = requests.get('https://www.jianshu.com')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)
# 这里分别打印输出status_code属性得到状态码，输出headers属性得到响应头，输出cookies属性得到Cookies，输出url属性得到URL，输出history属性得到请求历史。
# 状态码常用来判断请求是否成功，而requests还提供了一个内置的状态码查询对象requests.codes，示例如下：
r = requests.get('https://www.jianshu.com')
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
# 这里通过比较返回码和内置的成功的返回码，来保证请求得到了正常响应，输出成功请求的消息，否则程序终止。
