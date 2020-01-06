import urllib.request
import random
import re
from bs4 import BeautifulSoup
import crawler_make_header as smh

'''
用于从西刺代理提供免费代理池，只需要关注save_proxy和get_random_ip两个服务
前者是爬取新的代理，后者是从代理池中随机挑选一个
'''

def get_ip_list(obj):
    '''
    从网页数据中提取代理地址
    :param obj: 免费代理地址的网页爬取response
    :return: 代理IP列表
    '''
    ip_text = obj.findAll('tr', {'class': 'odd'})  # 在tr的tag中，class=odd
    ip_list = []
    for i in range(len(ip_text)):
        ip_tag = ip_text[i].findAll('td')
        ip_port = ip_tag[1].get_text() + ':' + ip_tag[2].get_text()  # 把IP和port联合起来
        ip_list.append(ip_port)
    # print("共收集到了{}个代理IP".format(len(ip_list)))
    # print(ip_list)
    return ip_list  # 爬取到的代理IP列表


def get_random_ip(proxy_path):
    '''
    随机从代理IP文本中提取一个
    :return: 一个随机的代理IP
    '''
    ip_ = open(proxy_path, 'r').readlines()  # 打开代理IP文件，在项目的Reference文件夹中
    ip_list = [re.sub(r'\n', '', str(i)) for i in ip_]  # 重构列表
    random_ip = 'http://' + random.choice(ip_list)  # 随机选择一个
    proxy = {'http:': random_ip}  # 构造成字典的形式，给urllib使用
    return proxy
    # print('check point: get_proxy')


def get_proxy(proxy):
    '''
    only run once for a day, save a self.bsObjct for proxy pool
    用于从代理ip网页爬取代理ip
    :return:
    '''
    url = 'http://www.xicidaili.com/nn'
    headers = {}
    headers["User-Agent"] = smh.make_agent('')
    headers["Upgrade-Insecure-Requests"] = 1
    headers["Accept-Language"] = 'zh-cn'
    headers["Connection"] = 'keep-alive'
    headers["Accept"] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'  # 构建伪浏览器请求头
    headers["Host"] = 'www.xicidaili.com'
    headers["Referer"] = 'www.xicidaili.com'
    proxy_support = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    bsObj = BeautifulSoup(response, 'lxml')
    return bsObj  # 网页数据


def save_proxy(origin_path):
    '''
    用于保存代理ip文件，这个程序可以定期启动一次，更新ip
    :return:
    '''
    proxy = get_random_ip('./References/proxy.txt')
    print(proxy)
    bsObj = get_proxy(proxy)
    ip_list = get_ip_list(bsObj)
    for i in ip_list:
        f = open(origin_path + '/References/proxy.txt', 'a')
        f.write(str(i) + '\n')
        f.close()
    print('proxy is saved')

if __name__ == '__main__':
    save_proxy('.')