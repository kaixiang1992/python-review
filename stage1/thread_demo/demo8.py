"""
2019/12/15 16:08
156.【多线程】实战-下载表情包之异步爬虫完成(爬虫--线程)
"""

import threading
from queue import Queue
import requests
from lxml import etree
from urllib import request
import re
import os


# TODO: 生产者
class Producer(threading.Thread):
    # TODO: 类属性
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.75 Safari/537.36 '
    }

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        # TODO: 调用父类构造函数
        super(Producer, self).__init__()
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while not self.page_queue.empty():
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.text)
        imgs = html.xpath('//div[@class="page-content text-center"]//a//img[@class!="gif"]')
        for img in imgs:
            img_url = img.get('data-original')
            img_alt = img.get('alt')
            img_alt = re.sub(r'[\?？\.。\*\+\!！,，]', '', img_alt)
            img_ext = os.path.splitext(img_url)[1]
            img_filename = img_alt + img_ext
            self.img_queue.put((img_url, img_filename))


# TODO: 消费者
class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__()
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            # TODO: url消息队列为空且图片消息队列为空退出循环
            if self.page_queue.empty() and self.img_queue.empty():
                break
            img_url, img_filename = self.img_queue.get()
            request.urlretrieve(img_url, './images/' + img_filename)
            print('%s 下载完成...' % (img_filename,))


def main():
    # TODO: url消息队列
    page_queue = Queue(100)
    # TODO: 图片消息队列
    img_queue = Queue(500)

    for x in range(1, 101):
        url = 'https://www.doutula.com/photo/list/?page=%s' % (x,)
        page_queue.put(url)

    # TODO: 5个生产者
    for x in range(0, 5):
        t = Producer(page_queue, img_queue)
        t.start()

    # TODO: 5个消费者
    for x in range(0, 5):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()
