"""
2019/11/17 18:04
99.【Python模块和包】__all__变量的作用
"""

# TODO: __all__
"""
1.如果是在模块中写了这个变量，将控制from 模块名字 import * 的行为.
2.如果是在__init__.py文件中有这个变量，那么将控制着 from 包 import * 的行为.
"""

__all__ = ['GLOBAL_STR', 'greet']

GLOBAL_STR = 'zhiliao ketang'


def greet():
    print('hello world!')


class Person(object):
    def __init__(self):
        print('init...')
