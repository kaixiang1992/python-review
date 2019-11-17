"""
2019/11/17 16:55
94.【Python】单例设计模式
"""

# TODO: 1.单例模式
"""
单例设计模式：某个类或者模型在整个程序运行期间最多只能有一个对象被创建
我们可以判断，如果User这个类没有创建过对象，那么就创建一个对象保存在某个地方
以后如果要再创建对象，我会去判断，如果之前已经创建了一个对象，那么就不再创建
而是把之前那个对象返回回去
"""


class User(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print('new....')
            cls.__instance = super(User, cls).__new__(cls)
        return cls.__instance

    def __init__(self, name):
        print('init...')
        self.name = name


user1 = User('zhiliao')
user2 = User('ketang')
print(id(user1))
print(id(user2))
print(id(user1) == id(user2))
print(user1.name)
print(user2.name)
