"""
2019/12/2 21:43
134.【Python魔术方法】属性访问控制魔术方法
"""

"""
属性访问控制魔术方法：

__getattr__魔术方法：
在访问一个对象的某个属性的时候，如果这个属性不存在，那么就会执行__getattr__方法，
将属性的名字传进去。如果这个属性存在，那么就不会调用__getattr__方法.

__setattr__魔术方法：
只要给一个对象的属性设置值，那么就会调用这个方法。但要注意的是，不要在这个方法中
调用self.xxx=xxx的形式，因为会产生递归。如果想要给对象的属性设置值有两种方式：
1）使用self.__dict__[name] = value 这个魔术属性.
2）使用super().__setattr(name, value)__依赖基类的方式来实现赋值.

__getattribute__魔术方法：
只要你访问一个对象的属性，不管这个属性存不存在都会执行这个方法，所以在写这个方法的
时候要小心循环调用。使用`super(类名, self).__getattribute__(item)`来避免产生死循
环的递归，这个方法只能在新式类中使用，不能在旧式类中使用。
"""
"""
__getattr__与__getattribute__区别：
1. __getattr__只有属性不存在的时候才会调用。
2. __getattribute__不管属性存不存在都会调用。
"""
import logging


class Person(object):
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.is_adult = False  # TODO: 是否成年

    def __getattr__(self, item):
        # if item == 'age':
        #     return 18
        # else:
        #     raise AttributeError('%s 属性不存在..' % item)

        """
        # 0.1 pname
        # 0.2 pname可以使用，但是会警告，在这个版本以后推荐使用name属性
        # 0.3 pname不能使用
        """
        if item == 'pname':
            logging.warning('pname可以使用，在下一个版本中不再使用这个属性，在这个版本以后推荐使用name属性...')
            return self.name
        else:
            raise AttributeError('%s 属性不存在..' % item)

    def __setattr__(self, key, value):
        # TODO: RecursionError: maximum recursion depth exceeded while calling a Python object
        # TODO: 达到最大递归层数
        # if key == 'name':
        #     self.name = 'zhiliao'

        # TODO: 调用方式1：使用__dict__魔术属性
        # self.__dict__[key] = value

        # TODO: 调用方式2：使用super().__setattr__依赖基类实现赋值
        super(Person, self).__setattr__(key, value)
        if key == 'age':
            # TODO: 调用无递归，正常改写语法
            # if value >= 18:
            #     self.is_adult = True
            # else:
            #     self.is_adult = False
            # print(self.is_adult)

            if value >= 18:
                self.__dict__['is_adult'] = True
            else:
                self.__dict__['is_adult'] = False

    def __getattribute__(self, item):
        # TODO: RecursionError: maximum recursion depth exceeded while calling a Python object
        # TODO: 达到最大递归层数
        # return self.__dict__[item]
        return super(Person, self).__getattribute__(item)


p1 = Person('zhiliao')
# print(p1.name)  # TODO: zhiliao
# print(p1.age)   # TODO: 18
# print(p1.country)   # TODO: AttributeError: country 属性不存在..

# print(p1.pname)  # TODO: zhiliao


p1.age = 19
print(p1.pname)  # TODO: zhiliao
print(p1.age)  # TODO: 19
print(p1.is_adult)  # TODO: True

print(p1.abc)  # TODO: AttributeError: abc 属性不存在..
