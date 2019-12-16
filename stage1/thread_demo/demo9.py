"""
2019/12/15 22:45
158.【多线程】作业-多线程下载百思不得姐段子爬虫作业(爬虫--线程)
"""

import threading
from queue import Queue
import json
from lxml import etree
import requests

JOKES = []  # TODO: 全局joke变量


# TODO: 生产者
class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.75 Safari/537.36 '
    }

    def __init__(self, page_queue, joke_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue  # TODO: url消息队列
        self.joke_queue = joke_queue  # TODO: 段子队列

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url, headers=self.headers)
        html = etree.HTML(response.text)
        jokes = html.xpath('//div[@class="j-r-list"]//li//div[@class="j-r-list-c-desc"]//a')
        for joke in jokes:
            href = 'http://www.budejie.com%s' % (joke.get('href'),)
            text = joke.xpath('.//text()')
            text = '\n'.join(text).strip()
            self.joke_queue.put((href, text))


# TODO: 消费者
class Consumer(threading.Thread):
    def __init__(self, page_queue, joke_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        global JOKES
        while True:
            try:
                href, text = self.joke_queue.get(timeout=2)
                JOKES.append(dict(href=href, text=text))
            except Exception as error:
                with open('jokes.json', 'w', encoding='utf-8') as fp:
                    json.dump(JOKES, fp, ensure_ascii=False)
                break


def main():
    page_queue = Queue(10)  # TODO: url消息队列
    joke_queue = Queue(100)  # TODO: 段子队列

    for x in range(1, 11):
        url = 'http://www.budejie.com/text/%s' % (x,)
        page_queue.put(url)

    # TODO: 5个生产者
    for x in range(0, 5):
        t = Producer(page_queue, joke_queue)
        t.start()

    # TODO: 5个消费者
    for x in range(0, 5):
        t = Consumer(page_queue, joke_queue)
        t.start()


if __name__ == '__main__':
    main()
