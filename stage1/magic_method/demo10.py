"""
2019/12/6 23:42
138.【Python魔术方法】pickle魔术方法
"""

"""
序列化对象：
Python中，如果要将一个对象存储到硬盘中，需要使用`pickle`模块，
其中`dump`方法可以将一个对象存储到硬盘中
`load`方法可以从硬盘中加载一个对象。

Python许多内置的数据结构是可以直接序列化的，
比如：字典(str)、列表(list)、元祖(tuple)、字符串(str)、序列(set)
"""
import pickle

# TODO: pickle魔术方法基本使用: 写入对象到磁盘中
data = {
    'foo': [1, 2, 3],
    'bar': ('hello', 'world'),
    'baz': True
}

with open('data.pkl', 'wb') as fp:
    pickle.dump(data, fp)

# TODO: pickle魔术方法基本使用：load从硬盘中加载一个对象

with open('data.pkl', 'rb') as fp:
    load_obj = pickle.load(fp)
    print(load_obj)

# TODO: 2.自定义可持续化对象
"""
自己定义的类对象，默认情况下是不能持续化的。如果想要让自定义的对象可持续化，那么应该实现
两个魔术方法：
__getstate__：这个魔术方法是在把对象存储到硬盘中的时候会调用的，会将这个方法的返回值存储
进去，返回值是可以持续化的数据类型，比如：字典、列表、字符串等等。
__setstate__: 这个魔术方法是从硬盘中加载对象的时候，会调用，会将之前存储进去的值，通过参
数的形式传递进来。
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
    把对象存储到硬盘中的时候会调用的
    """

    def __getstate__(self):
        print('__getstate__...')
        return {'name': self.name, 'age': self.age}

    """
    从硬盘中加载对象的时候会调用的
    """

    def __setstate__(self, state):
        print('__setstate__...')
        print(state)
        self.name = state.get('name')
        self.age = state.get('age')

    def __str__(self):
        return 'Person: (%s, %s)' % (self.name, self.age)


p1 = Person('zhiliao', 18)
print('-' * 50)
print(id(p1))
with open('./person.pkl', 'wb') as fp:
    pickle.dump(p1, fp)

with open('./person.pkl', 'rb') as fp:
    load_obj = pickle.load(fp)
    print('=' * 50)
    print(id(load_obj))
    print(load_obj)
