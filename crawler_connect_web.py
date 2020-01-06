import urllib.request
import requests

'''
用于爬虫联网，有urllib，get，post三种方法
'''

def urllib_request_web(link, header, proxy, decode = 'utf-8', time_out = 30):
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    request = urllib.request.Request(url=link, headers=header)
    response = urllib.request.urlopen(request, timeout=time_out)
    return str(response.read().decode(decode))

def get_web(link, request_data, header, proxy, decode = 'utf-8'):
    response = requests.get(url=link, data=request_data, headers=header, proxies=proxy)
    data = response.content.decode(decode)
    return data

def get_post(link, request_data, header, proxy, decode = 'utf-8'):
    response = requests.post(url=link, data=request_data, headers=header, proxies=proxy)
    data = response.content.decode(decode)
    return data