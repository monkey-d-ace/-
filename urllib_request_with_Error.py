#!/usr/bin/env python3
# -*- encoding=UTF-8 -*-
# urllib的error模块定义了由request模块产生的异常。如果出现了问题，request模块便会抛出error模块中定义的异常。
# URLError类来自urllib库的error模块，它继承自OSError类，是error异常模块的基类，由request模块产生的异常都可以通过捕获这个类来处理。
# 它具有一个属性reason，即返回错误的原因。
import urllib.request, urllib.error
try:
	response = urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError as e:
	print(e.reason)
# 我们打开一个无法访问的页面，按理来说应该会报错，但是这时我们捕获了URLError这个异常。程序没有直接报错，而是输出了错误原因，通过如上操作，我们就可以避免程序异常终止，同时异常得到了有效处理。
# HTTPError是URLError的子类，专门用来处理HTTP请求错误，比如认证请求失败等。它有如下3个属性。
# code：返回HTTP状态码，比如404表示网页不存在，500表示服务器内部错误等。
# reason：同父类一样，用于返回错误的原因。
# headers：返回请求头。
# 因为URLError是HTTPError的父类，所以可以先选择捕获子类错误，再去捕获父类的错误。
try:
	response = urllib.request.urlopen('https://www.google.com')
except urllib.error.HTTPError as e:
	print(e.reason, e.code, e.headers, seq='\n')
except urllib.error.URLError as e:
	print(e.reason)
else:
	print("处理成功")
# 这样就可以做到先捕获HTTPError，获取它的错误状态码，原因、headers等信息。如果不是HTTPError异常，就会捕获URLError异常，输出错误原因。最后用else来处理正常的逻辑。这是一个较好的异常处理写法。