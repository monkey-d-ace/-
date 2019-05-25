#!/usr/bin/env python3
import requests
from lxml import etree

class Login(object):
    def __init__(self):
        self.headers = {
                'Referer': 'http://192.168.4.168:10080/users/sign_in',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
                'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                'Accept-Encoding': "gzip, deflate",
                'Accept-Language': "zh-CN,zh;q=0.9",
                'Host': "192.168.4.168:10080"
                }
        self.login_url = "http://192.168.4.168:10080/users/sign_in"
        self.session = requests.Session()
        self.post_url = "http://192.168.4.168:10080/users/sign_in"

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath("//*[@id='new_user']/input[2]/@value")[0]
        print(token)
        return token

    def login(self, email, password):
        post_data = {
                'utf8': '✓',
                'authenticity_token': self.token(),
                'user[login]': email,
                'user[password]': password,
                'user[remember_me]': '0'
                }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            print(response.text)
        else:
            print("error")
            print(post_data)


if __name__ == "__main__":
    login = Login()
    login.login(email="wangfengshu805@berrygenomics.com", password="$521yangli")
#r = requests.get("http://192.168.4.168:10080/Analysis-System/data-analysis-system", auth=("wangfengshu805$berrygenomics.com", "$521yangli"))
#print(r.status_code)
#print(r.text)

