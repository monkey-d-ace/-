#!/usr/bin/env python3
import urllib.request
# 这里我们以爬取pharmgkb官网首页为例

response = urllib.request.urlopen('https://www.pharmgkb.org')
print(response.read().decode('utf-8'))
# 这里我们只用了两行代码，便完成了pharmgkb官网的抓取，输出了网页的源代码。

# 接下来，我们看看response返回的是什么。通过使用type()方法输出响应的类型。
print(type(response))
# 可以发现，它是一个HTTPResponse类型的对象，主要包含read()、readinto()、getheader(name)、getheaders()、fileno()等方法，以及msg、version、status、reason、debuglevel、closed等属性。
# 得到这个对象之后，我们把它赋值为response变量，然后就可以调用这些方法和属性
