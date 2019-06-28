# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re



html_doc = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <b>测试</b>
        <p class="title">
            <b>The Dormouse's story</b>
        </p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
        </p>

        <p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, "html.parser")
print("获取所有链接")
links = soup.find_all('a')
for link in links:
    print(link.name,link.get('href'),link.get_text())

print("获取lacie的链接")

link_node = soup.find_all('a',href="http://example.com/lacie")
print(link_node[0].name,link_node[0].get('href'),link_node[0].get_text())

print("匹配正则")

link_node = soup.find_all('a',href=re.compile(r"ill"))
for link in link_node:
    print(link.name,link.get('href'),link.get_text())


