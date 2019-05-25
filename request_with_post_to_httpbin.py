#!/usr/bin/env python3
# 使用requests实现POST请求同样非常简单
import requests
data = {'name': 'germey', 'age': 28}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)

