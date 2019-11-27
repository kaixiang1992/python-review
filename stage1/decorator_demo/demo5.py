"""
2019/11/27 20:54
123.【Python装饰器】装饰器实现Flask的url映射
"""

# TODO: 装饰器实现Flask的url映射
"""
装饰器模拟实现Flask的Url映射
"""
from functools import wraps

USER = {
    'is_login': True
}


# TODO: 登录拦截装饰器
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if USER.get('is_login'):
            func(*args, **kwargs)
        else:
            print('跳转到登录页面')

    return wrapper


class Flask(object):
    def __init__(self):
        """
        {
            '/': 'hello',
            '/article': 'article_list',
            '/edit': 'edit_article'
        }
        """
        self.url_map = {}

    def route(self, url):
        def outer_wrapper(func):
            # TODO: url不在self.url_map中进行存储
            if url not in self.url_map:
                self.url_map[url] = func.__name__
            print(self.url_map)

            @wraps(func)
            def inner_wrapper(*args, **kwargs):
                print('func.__name__ {}, args {}, kwargs {}, 执行中...'.format(func.__name__, args, kwargs))
                func(*args, **kwargs)

            return inner_wrapper

        return outer_wrapper

    def run(self):
        while True:
            url = input('请输入页面地址url: ')
            # TODO: 输入地址在self.url_map中
            if url in self.url_map:
                exec(self.url_map[url] + '()')
            else:
                # TODO: -1退出while循环
                if url == '-1':
                    break
                print('页面地址不存在，404!...')


app = Flask()


# TODO: app.route('/')(hello)()

@app.route('/')
def hello():
    print('你好, 世界!')


# TODO: app.route('/')(article_list)()

@app.route('/article')
def article_list():
    print('文章列表...')


# TODO: app.route('/edit')(login_required(edit_article))()

@app.route('/edit')
@login_required
def edit_article():
    print('文章修改成功...')


if __name__ == '__main__':
    app.run()
