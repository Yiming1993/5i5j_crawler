import re
import json
from bs4 import BeautifulSoup

'''
负责解析response数据
'''

def Beautiful_extract(html, html_decode_type = 'html5lib'):
    soup = BeautifulSoup(html, html_decode_type)
    return soup

def json_extract(string, encoding = 'utf-8'):
    return json.loads(string, encoding=encoding)

def format_control(string, control_list):
    string = re.sub(control_list[0], control_list[1], str(string))
    return string

def locate_tag(string, locate_rule, return_type = 'single'):
    if return_type == 'single':
        data = re.findall(locate_rule, string)
        if data == []:
            return []
        else:
            return re.findall(locate_rule, string)[0]
    if return_type == 'all':
        return re.findall(locate_rule, string)
    else:
        raise ValueError('no idea what to export')

def str2dict(string):
    return json.loads(string, encoding='utf-8')