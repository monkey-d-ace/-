#!/usr/bin/env python3
import http.cookiejar, urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.pharmgkb.org')
for item in cookie:
	print(item.name + "=" + item.value)
	
# 首先，我们必须声明一个CookieJar对象。接下来，就需要利用HTTPCookieProcessor来构建一个Handler，最后利用build_opener()方法构建出Opener，执行open()函数即可。
# 可以看到，这里输出了每条Cookie的名称和值。
# Cookie实际上也可以输出成文本形式保存。
filename = 'cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.pharmgkb.org')
cookie.save(ignore_discard=True, ignore_expires=True)
# 这时CookieJar就需要换成MozillaCookieJar，它在生成文件时会用到，是CookieJar的子类，可以用来处理Cookies和文件相关的事件，比如读取和保存Cookies，可以将Cookies保存成Mozilla型浏览器的Cookies格式。
# 另外，LWPCookieJar同样可以读取和保存Cookies，但是保存的格式和MozillaCookieJar不一样，它会保存成libwww-perl(LWP)格式的Cookies文件。
# 要保存成LWP格式的Cookies文件，可以在声明时就改为:
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.pharmgkb.org')
cookie.save(ignore_discard=True, ignore_expires=True)

# 那么生成Cookies文件后，怎样从文件中读取并利用呢？下面我们以LWPCookieJar格式为例来看一下：
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.pharmgkb.org')
print(response.read().decode('utf-8'))
# 可以看到，这里调用了load()方法来读取本地的Cookies文件，获取到了Cookies的内容。不过前提是我们首先生成了LWPCookieJar格式的Cookies，并保存成文件，然后读取Cookies之后同样的方法构建Handler和Opener即可完成操作。
