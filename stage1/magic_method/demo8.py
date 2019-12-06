"""
2019/12/6 23:02
136.【Python魔术方法】可调用的对象魔术方法
"""

"""
可调用的对象：
允许一个类的实例像函数一样被调用。实质上说，这意味着x()与x.__call()__是相同的。
注意__call__参数可变。这意味着你可以定义__call__为其他你想要的的函数，无论有多少个参数。
"""


# TODO: 1.Django实例

def index():
    return "index page."


class IndexView(object):
    def __call__(self, *args, **kwargs):
        return 'index view page.'


def visit_view(view):
    """

    :param view: 接收可能为函数，也可能为对象。不关心调用即可。鸭子类型。
    :return:
    """
    print(view())


visit_view(index)
visit_view(IndexView())


# TODO: 2.示例2

class Coornidate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: __call__魔术方法:
    def __call__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Coornidate: (%s, %s)' % (self.x, self.y)


position = Coornidate(1, 2)
position(6, 9)
print(position)
