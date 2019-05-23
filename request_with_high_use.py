#!/usr/bin/env python3
# 高级用法：在前一节中，我们了解了requests的基本用法，如基本的GET、POST请求以及Response对象。本节中，我们再来了解一下requests的一些高级用法，如文件上传、Cookies设置、代理设置等。
import requests
files = {'file': open('favicon.ico', 'rb')}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)
# 这个网站会返回响应，里面包含files这个字段，而form字段是空的，这证明文件上传部分会单独有一个files字段来标识。

# 2.Cookies：前面我们使用urllib处理过Cookies，写法比较复杂，而有了requests，获取和设置Cookies只需一步即可完成。
r = requests.get("http://www.baidu.com")
print(r.cookies)
for key, value in r.cookies.items():
    print(key + '=' + value)
# 这里我们首先调用cookies属性即可成功得到Cookies，可以发现它是RequestCookieJar类型。然后用items()方法将其转化为元组组成的列表，遍历输出每一个Cookie的名称和值，实现Cookie的遍历解析。当然我们也可以直接用Cookie来维持登录状态。

cookies = '_gitlab_session=4dac5ed133294ee6091abfa713f211f6'
headers = {
        'Host': 'http://192.168.4.168:10080/dashboard/todos',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
        }
response = requests.get('http://192.168.4.168:10080/dashboard/todos', headers=headers)
# print(response.text)
print(response.cookies)
