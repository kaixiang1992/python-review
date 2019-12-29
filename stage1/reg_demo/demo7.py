"""
2019/12/29 19:17
167.【正则表达式】作业-糗事百科爬虫作业
"""
import requests
import re


def parse_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    response = requests.get(url, headers)
    text = response.text
    print(text)

def main():
    url = 'http://www.lovehhy.net/Joke/Detail/QSBK/2'
    parse_page(url)


if __name__ == '__main__':
    main()
