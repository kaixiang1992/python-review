"""
2019/11/26 23:43
123.【Python装饰器】装饰器实现Flask的url映射
"""

from flask import Flask, request, escape

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get('name', '世界')
    return f'你好, {escape(name)}'


@app.route('/article')
def article_list():
    return f'文章列表'


if __name__ == '__main__':
    app.run()
