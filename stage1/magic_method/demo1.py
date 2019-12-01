"""
2019/12/1 18:29
129.【Python魔术方法】常规魔术方法
"""

"""
常规魔术方法：
__str__魔术方法：
在打印某个对象时，通常显示的是所属类的名字及其内存地址，不适合人类阅读。
如果你想在打印某个对象的时候更加友好，那么你可以重写这个方法。

__repr__魔术方法：
这个魔术方法是用来表述一个对象的，用于给机器看的。
在终端命令行中：
在终端定义了一个类，然后初始化一个对象，然后直接输入这个对象接着按回车，这个时候会
使用__repr__魔术方法返回的值
在Pycharm编辑器中：
如果将一个对象创建完成后，方到一个列表中，然后再打印这个列表，那么会打印这个列表中
所有的对象，这时候会调用__repr__魔术方法
"""
"""
常用魔术属性：

__dict__: 这个属性装的是所有用户自定义的属性及属性值
    例：{'name': 'zhiliao', 'age': 18, 'country': 'china'}

dir()函数：可以获取所有属性包括Python内置的属性和用户自己添加的，只返回
属性名字。

"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.country = 'china'

    def __str__(self):
        return 'Person name is %s' % self.name

    def __repr__(self):
        return 'Person name is %s' % self.name


p1 = Person('zhiliao', 18)
p2 = Person('ketang', 20)
a = [p1, p2]
print(p1)
print(a)

# TODO: __dict__魔术属性

print(p1.__dict__)

# TODO: dir函数

print(dir(p1))
