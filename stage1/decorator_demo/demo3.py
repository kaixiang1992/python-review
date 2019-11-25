"""
2019/11/25 23:43
120.【Python装饰器】给装饰器传递参数
"""

# TODO: 1.带参数的装饰器
"""
装饰器也可以传递参数。只不过如果给装饰器传递参数了，那么就要
在这个装饰器中写两个方法(双层闭包)
"""

USER = {
    'is_login': True
}


def login_required(site='front'):
    def outer_wrapper(func):
        print(func.__name__)  # TODO: front_login、backend_login

        def wrapper(*args, **kwargs):
            if USER.get('is_login'):
                print(args)
                func(*args, **kwargs)
            else:
                if site == 'front':
                    print('跳转到前台登录页面...')
                else:
                    print('跳转到后台登录页面...')

        return wrapper

    return outer_wrapper


class Person(object):
    @login_required('front')
    def front_login(self, username):
        print('%s 用户前台系统登录成功...' % username)

    @login_required('backend')
    def backend_login(self, username):
        print('%s 用户后台系统登录成功...' % username)


p = Person()
p.front_login('test001')
# TODO: login_required('front')(front_login)(self, 'test001')
p.backend_login('admin001')
# TODO: login_required('backend')(backend_login)(self, 'admin001')
