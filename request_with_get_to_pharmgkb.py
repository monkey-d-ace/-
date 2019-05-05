#!/usr/bin/env python3
# HTTP中最常见的请求之一就是GET请求，下面首先来详细了解一下利用requests构建GET请求的方法。
import requests
r = requests.get('http://httpbin.org/get')
print(r.text)
# 可以发现，我们成功发起了GET请求，返回结果中包含请求头、URL、IP等信息。
# 那么，对于GET请求，如果要附加额外信息，一般怎样添加呢？利用params这个参数就好了。
data = {
        'name': 'germey',
        'age': 22
        }
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
# 通过运行的结果可以判断，请求的链接自动被构造成了:http://http.org/get?age=22&name=germey。另外，网页的返回类型实际上是str类型，但是它很特殊，是JSON格式的。所以，如果想直接解析返回结果，得到一个字典格式的话，可以直接调用json()方法。
print(type(r.text))
print(r.json())
print(type(r.json()))
# 可以发现，调用json()方法，就可以将返回结果是JSON格式的字符串转化为字典。但需要注意的是，如果返回结果不是JSON格式，便会出现解析错误，抛出json.decoder.JSONDecodeError异常。

