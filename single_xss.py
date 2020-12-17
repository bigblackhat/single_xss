# coding:utf-8
import requests
import copy
from urlparse import urlparse 
from time import sleep
import random
import json
import re

_version = 1.2
_author = "jijue"

def gen_user_agent():
    user_agent_list = """
                        Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)
                        Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)
                        Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)
                        Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)
                        Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)
                        Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))
                        Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)
                        Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)
                        """
    user_list = user_agent_list.strip().splitlines()
    user_list = [i.strip() for i in user_list]
    return random.choice(user_list)



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
        self.headers = {"user-agent":gen_user_agent()}

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

def wafdetect(url,params,headers,GET = True):
    with open("wafSignatures.json") as f:
        wafSignatures = json.load(f)
    noise = '<script>alert("XSS")</script>'
    params['xss'] = noise
    if GET:
        response = requests.get(url,params = params,headers = headers)
    else:
        response = requests.post(url,params = params)
    page = response.text
    code = response.status_code
    headers = response.headers
    if code >= 400:
        bestMatch = [0, None]
        for wafName, wafSignature in wafSignatures.items():
            score = 0
            pageSign = wafSignature['page']
            codeSign = wafSignature['code']
            headersSign = wafSignature['headers']
            if pageSign:
                if re.search(pageSign, page, re.I):
                    score += 1
            if codeSign:
                if re.search(codeSign, code, re.I):
                    score += 0.5  # increase the overall score by a smaller amount because http codes aren't strong indicators
            if headersSign:
                if re.search(headersSign, headers, re.I):
                    score += 1
            # if the overall score of the waf is higher than the previous one
            if score > bestMatch[0]:
                del bestMatch[:]  # delete the previous one
                bestMatch.extend([score, wafName])  # and add this one
        if bestMatch[0] != 0:
            return bestMatch[1]
        else:
            return None
    else:
        return None
        






def single_fuzz(url):
    if requests.get(url).status_code == 200:
        pass 
    else :
        print "url无法访问 响应码为%d" % (r.status_code)
        exit(0)
    urlp = url_parse(url)

    _waf = wafdetect(urlp.scheme + "://" + urlp.host + "/" + urlp.path,urlp.params,urlp.headers)

    if _waf:
        print "WAF detected: %s" % (_waf)
    else:
        print "Not Found WAF"
    for param_name in urlp.params.keys():
        paramslist = copy.deepcopy(urlp.params)
        paramslist[param_name] += "*"
        fuzzing(urlp.scheme,urlp.host,urlp.path,urlp.params)



payloads = ['<svg "ons>', '" onfocus="alert(1);', 'javascript:alert(1)']

# url = "http://127.0.0.1:8091/level1.php?name=1*&as=1"

url = "https://domgo.at/cxss/example/1?payload=abcd&sp=x"
res = requests.get(url)
response = res.text
scripts = re.findall(r'(?i)(?s)<script[^>]*>(.*?)</script>', response)
# print scripts
for script in scripts:
    script = script.split("\n");print script