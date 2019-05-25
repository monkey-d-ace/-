#!/usr/bin/env python3
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
        'name': 'germey'
        }
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
        }
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepared = s.prepare_request(req)
r = s.send(prepared)
print(r.text)

