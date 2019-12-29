"""
2019/12/29 18:46
166.【正则表达式】实战-古诗文网爬虫实战
"""

import requests
import re


def parse_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    text = response.text
    titles = re.findall(r'<div\s*class="cont".*?<b>(.*?)</b>', text, re.DOTALL)  # TODO: 名字
    dynasties = re.findall(r'<p\s*class="source".*?<a.*?>(.*?)</a>', text, re.DOTALL)  # TODO: 朝代
    authors = re.findall(r'<p\s*class="source".*?<a.*?<a.*?>(.*?)</a>', text, re.DOTALL)  # TODO: 作者
    content_tags = re.findall(r'<div\s*class="contson".*?>(.*?)</div>', text, re.DOTALL)  # TODO: 内容
    content = []
    for x in content_tags:
        x = re.sub('<.*>', '', x)
        content.append(x.strip())
    peoms = []
    for value in zip(titles, dynasties, authors, content):
        title, dynastie, author, peom = value
        peoms.append({
            'title': title,
            'dynastie': dynastie,
            'author': author,
            'peom': peom
        })
    print(peoms)


def main():
    url = 'https://www.gushiwen.org/default_1.aspx'
    parse_url(url)


if __name__ == '__main__':
    main()
