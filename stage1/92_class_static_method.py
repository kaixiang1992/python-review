"""
2019/11/17 15:57
92.【Python面向对象】类方法和静态方法
"""

"""
类方法：第一个参数必须是cls，这个cls代表的是当前这个类
静态方法：静态方法是属于类的，只能通过类名字调用。静态方法中不能调用类属性，
如果要调用，只能通过类名来调用.并且不需要传递对象self或者类cls.
静态方法使用场景：不需要修改类或者对象属性的时候，并且这个方法放在这个类中
可以让代码更加有管理性.
"""

class Person(object):
    country = 'china'

    def eat(self):
        print('hello world!')

    @classmethod
    def greet(cls):
        cls.country = 'earth'
        print('调用类方法...')

    @staticmethod
    def static_method():
        print('调用静态方法..')
        Person.country = 'usa'


# TODO: 1.实例方法
p1 = Person()
p1.eat()

# TODO: TypeError: eat() missing 1 required positional argument: 'self'
# Person.eat()

# TODO: 2.类方法
# TODO: 实例调用
p1.greet()
# TODO: 类调用
Person.greet()


# TODO: 3.静态方法
# TODO: 实例调用
p1.static_method()
# TODO: 类调用
Person.static_method()

print(Person.country)