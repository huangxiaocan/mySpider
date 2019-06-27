# -*- coding:utf-8 -*-
# author：huangc
# 博客：http://www.boyumanong.top
# 仅做学习用途
import urllib.request
import re

def getvideo(page):
    req = urllib.request.Request('http://www.budejie.com/video/%s' % page)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
    html = urllib.request.urlopen(req).read()
    print(html)
    reg = r'data-mp4="(.*?)"' #r目的是以原生字符串显示
    result = re.findall(reg,html.decode('utf-8'))
    print(result)
    for i in result:
        filename = i.split('/')[-1]
        print('正在下载%s' % filename)
        urllib.request.urlretrieve(i,"D:/mp4/%s" % filename) #下载

for i in range(1,101):
    getvideo(i)
