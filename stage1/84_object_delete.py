"""
2019/11/16 20:25
84.【Python面向对象】析构函数和引用计数
"""
import sys

# TODO: 1.析构函数
"""
析构函数，也即__del__方法，只要这个对象在内存中即将消灭的时候，就会调用这个方法。
"""


class Person(object):
    def __init__(self):
        print('这是构造函数')
        self.name = 'zhiliao'
        self.fp = open('./del.txt', 'w', encoding='utf-8')

    def greet(self):
        print('hello, 我的名字是：%s' % self.name)

    def write(self, message):
        self.fp.write(message)

    def __del__(self):
        self.fp.close()
        print('这是析构函数')


p = Person()    # TODO: 计数 +1
p.greet()
p.write('hello world!')
print(sys.getrefcount(p))   # TODO: 计数 +1

p2 = p  # TODO: 计数 +1
print('=' * 50)


# TODO: 2.引用计数
"""
Python中的对象是使用引用计数的方式实现的。也即没有任何对象引用到一块内存，
那么Python将会把这块内存回收。
可以使用sys.getrefcount(object)来获取一个对象的引用计数。
"""

print(sys.getrefcount(p))

