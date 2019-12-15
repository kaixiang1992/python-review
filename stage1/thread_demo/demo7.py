"""
2019/12/15 15:13
155.【多线程】实战-下载表情包之同步爬虫完成(线程)
"""

import requests
from lxml import etree
import os
import re
from urllib import request


def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.75 Safari/537.36 '
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    imgs = html.xpath('//div[@class="page-content text-center"]//a//img[@class!="gif"]')
    for img in imgs:
        img_url = img.get('data-original')
        img_alt = img.get('alt')
        img_alt = re.sub(r'[\?？\.。\*\+\!！,，]', '', img_alt)
        img_ext = os.path.splitext(img_url)[1]
        img_filename = img_alt + img_ext
        # TODO: 下载图片
        request.urlretrieve(img_url, './images/' + img_filename)


def main():
    for x in range(1, 101):
        url = 'https://www.doutula.com/photo/list/?page=%s' % (x, )
        parse_page(url)
        break


if __name__ == '__main__':
    main()
