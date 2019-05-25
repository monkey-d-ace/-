#!/usr/bin/env python3
import requests
from requests.auth import HTTPBasicAuth
r = requests.get("http://cnv.test", auth=HTTPBasicAuth("root@berrygenomics.com", "secret"))
print(r.status_code)


r = requests.get("http://cnv.test", auth=("root@berrygenomics.com", "secret"))
print(r.status_code)

