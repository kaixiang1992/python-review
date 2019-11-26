"""
2019/11/26 23:02
122.【Python面向对象进阶】动态添加属性和方法
"""
import types


class Person(object):
    # TODO: 6.__slots__魔术变量: 元祖或列表
    # __slots__ = ['name', 'age', 'country', 'run']
    __slots__ = ('name', 'age', 'country', 'run')

    def __init__(self, name):
        self.name = name


p = Person('zhiliao')

# TODO: 1.动态添加属性
print('1.动态添加属性...')
# TODO: 1.1 对象名.属性名添加
p.age = 18
print(p.age)

# TODO: 1.2 使用setattr函数添加
setattr(p, 'country', 'china')
print(p.country)

# TODO: 1.3 hasattr用来判断一个对象是否有某个属性
if hasattr(p, 'country'):
    print(True)
else:
    print(False)

# TODO: 1.4 getattr是用来访问这个对象的某个属性，并且这个属性不存在的时候，
#  可以指定一个默认值，不指定默认值将抛出AttributeError属性错误
# getattr(p, 'height')
print(getattr(p, 'height', '自定义属性读取错误...'))
print('=' * 50)

# TODO: 2.动态添加实例方法
"""
如果想在运行的时候添加方法，这时候应该使用到types.MethodType这个方法
使用方法：
当前实例化对象.方法名 = types.MethodType(自定义方法名, 当前实例化对象)
"""
print('2.动态添加实例方法...')


def run(self):
    print('%s 在奔跑...' % self.name)


p.run = types.MethodType(run, p)
p.run()
print('=' * 50)

# TODO: 3.动态添加类方法
"""
动态添加类方法，是把这个方法添加给类。因此添加类方法的时候不是给对象添加的，而是给类添加的。
不需要使用types.MethodType,直接将这个函数赋值给类就可以了，但是需要使用@classmethod装饰器
将这个方法设置为一个类方法。
"""
print('3.动态添加类方法...')


@classmethod
def MyClassMethod(cls):
    print('动态添加自定义类方法成功...')


Person.MyClassMethod = MyClassMethod
Person.MyClassMethod()
print('=' * 50)

# TODO: 4.动态添加静态方法
"""
动态添加静态方法，是把这个方法添加给类的。因此也是直接给类添加的，使用@staticmethod这个装饰器.
"""
print('4.动态添加静态方法...')


@staticmethod
def add(a, b):
    return a + b


Person.add = add
print(Person.add(1, 4))
print('=' * 50)

# TODO: 5.动态删除属性和方法
"""
del 对象.属性名/方法名
delattr(对象, "属性名/方法名")
"""
print('5.动态删除属性和方法...')

del p.name
print(p.__dir__())
# print(p.name)  # TODO: AttributeError

delattr(p, 'run')
# p.run()  # TODO: AttributeError
print(p.__dir__())
print('=' * 50)

# TODO: 6.__slots__魔术变量
"""
有时候我们想指定某个类的对象，只能使用我指定的这些属性，
不能随便添加其他的属性，那么这时候就可以使用__slots__魔术变量。
这个魔术变量是一个列表或者一个元组，里面存放属性的名字，
以后在对象外面，就只能添加这个魔术变量中指定的属性，不能添加其他属性
"""
print('__slots__魔术变量...')

try:
    setattr(p, 'weight', 160)
except AttributeError as error:
    print(error)
