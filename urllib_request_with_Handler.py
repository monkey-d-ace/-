#!/usr/bin/env python3
# 首先介绍一下urllib.request模块里的BaseHandler类，它是所有其他Handler的父类，它提供了最基本的方法，例如default_open()、protocol_request()等。
# 有些网站在打开时就会弹出提示框，直接提示你输入用户名和密码，验证成功后才能查看页面。那么，如果要请求这样的页面，该怎么办呢？借助HTTPBasicAuthHandler就可以完成。
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
username = 'wangfengshu805@berrygenomics.com'
password = '$521yangli'
url = 'http://192.168.4.168:10080/Analysis-System/Tool/tree/master'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    # print(html)
    print(result.status)
    print(result.getheaders())
    print(result.getheader('Server'))
except URLError as e:
    print(e.reason)
# 这里首先实例化HTTPBasicAuthHandler对象，其参数是HTTPPasswordMgrWithDefaultRealm对象。它利用add_password()添加进去用户名和密码，这样就建立了一个处理验证的Handler。接下来，利用这个Handler并使用build_opener()方法构建一个Opener，这个Opener在发送请求时就相当于已经验证成功了。接下来，利用Opener的open()方法打开链接，就可以完成验证了。这里获取到的结果就是验证后的页面源码内容。
