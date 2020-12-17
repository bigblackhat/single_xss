# coding:utf-8
import requests
import socks

"""
[对于 Python 抓取 Google 搜索结果的一些了解](https://juejin.cn/post/6844903750939705357)
"""

query = "intitle:\"index of\" \"backup files\"".replace(" ","+")
headers = {'user-agent': "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"}

response = requests.get("http://www.google.com.hk/search?q={}&btnG=Search&gbv=1&num=2".format(query), proxies={
    'http': 'socks5://127.0.0.1:1086',
    'https': 'socks5://127.0.0.1:1086'
},headers=headers)
# print response.status_code
print(response.text.encode("utf-8"))

# file:///url?q=https://mail.mfmr.gov.so/Backup%2520Files/&sa=U&ved=2ahUKEwiVwMzSp9TtAhVTzYsBHf4KC5sQFjABegQIBxAB&usg=AOvVaw23ATNOqn0BAu_74lwigT0h

# https://www.google.com.hk/search?newwindow=1&safe=strict&sxsrf=ALeKk00Zx9LlRgaVpVFVUO-__TOVNsJn4Q%3A1608184140658&ei=TPHaX_TNJ6WUmAWs0rvoDg&q=n&oq=n&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIECCMQJzIECCMQJzIFCAAQkQIyBQgAEJECMggIABCxAxCDATIICAAQsQMQgwEyBQguELEDMggILhCxAxCDATIFCAAQsQNQm_IPWJvyD2C0-w9oAHAAeACAAYACiAGAApIBAzItMZgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwj0o7_jqNTtAhUlCqYKHSzpDu0Q4dUDCA0&uact=5