"""
2019/11/17 10:50
89.【Python面向对象】多继承及其注意事项
"""


# TODO: 1.多继承及其注意事项
"""
在新式类中，如果多继承，那么采用C3算法，使用的是广度优先的算法，打印
class.__mro__可以看到基类执行的顺序。
例： Luozi.__mro__
(<class '__main__.Luozi'>, <class '__main__.Ma'>, <class '__main__.Lv'>, <class 'object'>)

super(class, self).方法名([可选参数])是按照__mro__的基类顺序执行
如果不想按照__mro__的顺序执行父类的方法，那么可以通过以下方式执行class.方法名([self, 可选参数])
例： Lv.eat(self)
"""

class Ma(object):
    def run(self):
        print('马在奔跑...')

    def eat(self):
        print('马在吃草...')


class Lv(object):
    def lamo(self):
        print('驴在拉磨...')

    def eat(self):
        print('驴在吃麦秆...')


class Luozi(Ma, Lv):
    def eat(self):
        # TODO: 如果不想按照__mro__的顺序执行父类的方法，
        #  那么可以通过以下方式执行class.方法名([self, 可选参数])
        # super(Luozi, self).eat()
        Lv.eat(self)
        print('骡子在吃稻谷...')



luozi = Luozi()
luozi.eat()
# TODO: (<class '__main__.Luozi'>, <class '__main__.Ma'>, <class '__main__.Lv'>, <class 'object'>)
# print(Luozi.__mro__)