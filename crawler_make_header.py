import random

'''
提供伪造请求头的方法
'''

def make_agent():
    agent_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0"
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201"
    ]

    return random.choice(agent_list)

# def make_cookie(link, time_stamp = True, Jsession = True):
#     cookie = ''
#     if time_stamp == True:
#         import datetime