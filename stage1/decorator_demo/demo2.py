"""
2019/11/25 22:59
119.【Python装饰器】被装饰的函数带有参数
"""

# TODO: 1.什么是装饰器
"""
装饰器利用了函数也可以作为参数和闭包的特性，可以让我们的函数在执行
之前或者执行之后方便的添加一些代码。
"""

USER = {
    'is_login': False
}


def login_required(func):
    def wrapper(*args, **kwargs):
        if USER.get('is_login'):
            # print(args)
            # print(kwargs)
            func(*args, **kwargs)
        else:
            print('跳转到登录页面...')

    return wrapper


class Person(object):

    @login_required
    def edit_user(self, username):
        print('%s,修改用户名成功...' % username)

    @login_required
    def add_article(self, title, content):
        print('title is %s, content is %s' % (title, content))
        print('发布文章成功...')


p = Person()
print(id(p))
p.edit_user('zhiliao')
# TODO: login_required(edit_user)(self, username)
p.add_article('zhiliao ketang', 'python class')
# TODO: login_required(edit_user)(self, title, content)
