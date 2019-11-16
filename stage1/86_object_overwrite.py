"""
2019/11/16 21:08 待整理语雀笔记
86.【Python面向对象】重写父类的方法
"""

# TODO: 1.重写父类的方法
"""
1.如果父类的方法不能满足子类的需求，那么可以重写这个方法，以后对象
调用同名方法的时候，就会执行子类的这个方法.
2.虽然父类的方法不能完全满足子类的需求，但是父类的方法的代码还是需
要执行，那么可以通过super这个函数来调用父类的方法.
3.super的用法: super(类名, self).方法名([可选参数])
super(Student, self).__init__(name, age)
super(Student, self).eat()
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('人在吃饭')


class Student(Person):
    def __init__(self, name, age):
        # TODO: 调用父类构造函数
        super(Student, self).__init__(name, age)
        print('学生初始化...')

    # TODO: 重写父类eat方法
    def eat(self):
        # TODO: 调用父类eat函数
        super(Student, self).eat()
        print('学生在吃饭...')

    def greet(self):
        print('hello, my name is {}, my age is {}.'.format(self.name, self.age))


student = Student('zhiliao', 18)
student.eat()
student.greet()
