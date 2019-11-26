"""
2019/11/26 22:44
121.【Python装饰器】wraps装饰器
"""
from functools import wraps

# TODO: 1.wraps装饰器
"""
采用之前的装饰器，会让我们的函数失去一些属性，比如函数名__name__，这样在一些代码中会产生错误。
如果我们想要用装饰器，并且仍想保留函数的一些属性，比如函数名__name__,那么可以使用wraps装饰器。
"""

USER = {
    'is_login': True
}


def login_required(func):
    @wraps(func)
    def warpper(*args, **kwargs):
        if USER.get('is_login'):
            func(*args, **kwargs)
        else:
            print('跳转到登录页面...')

    return warpper


class Person(object):
    @login_required
    def edit_user(self, username):
        print('%s 用户名修改成功' % username)

    @login_required
    def add_article(self, title, content):
        print('title is %s, content is %s, 文章发布成功' % (title, content))


p = Person()
# TODO: login_required(edit_user)(self, username) => warpper(self, username)
# p.edit_user('test001')
# print(p.edit_user.__name__)
# TODO: login_required(add_article)(self, username) => warpper(self, title, content)
# p.add_article('第一篇文章', '第一篇文章内容...')
# print(p.add_article.__name__)

print('使用wraps装饰器后...')
p.edit_user('test001')
print(p.edit_user.__name__)  # TODO: edit_user
p.add_article('第一篇文章', '第一篇文章内容...')
print(p.add_article.__name__)  # TODO: add_article
