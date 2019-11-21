"""
2019/11/19 23:26
113.【迭代器】迭代器和for循环底层原理

常见可迭代对象：
list、tuple、dict、set、str
"""

from collections.abc import Iterable, Iterator

# TODO: 1.判断一个对象是否可迭代
"""
使用isinstance()判断一个对象是否是Iterable的对象
判断一个对象是否是可迭代对象
实现__iter__内置方法
"""

# TODO: 列表是一个可迭代对象
ret = [1, 2, 3, 4]
print(isinstance(ret, Iterable))  # TODO: true

# TODO: 元组是一个可迭代对象
ret = (1, 2, 3, 4)
print(isinstance(ret, Iterable))  # TODO: true

# TODO: 字典是一个可迭代对象
ret = {'name': 'zhiliao', 'age': 18}
print(isinstance(ret, Iterable))  # TODO: true

# TODO: set序列是一个可迭代对象
ret = {1, 2, 3, 4, 5}
print(isinstance(ret, Iterable))  # TODO: true

# TODO: 字符串是一个可迭代对象
ret = '123'
print(isinstance(ret, Iterable))  # TODO: true

# TODO: int不是一个可迭代对象
ret = 123
print(isinstance(ret, Iterable))  # TODO: False

# TODO: 判断一个对象是否是可迭代对象
"""
实现__iter__内置方法
"""


class MyRange(object):
    def __iter__(self):
        pass


ret = MyRange()
print(isinstance(ret, Iterable))  # TODO: true

# TODO: 判断一个对象是否是迭代器对象
"""
使用isinstance()判断一个对象是否是Iterator对象
在python3中，实现了__next__方法和__iter__方法，并且这个方法返回了值的
对象，叫做迭代器对象。
如果迭代器没有返回值了，那么应该在__next__方法中抛出StopIteration异常。
"""


class MyRangeIter(object):
    def __iter__(self):
        pass

    def __next__(self):
        pass


ret = MyRangeIter()
print(isinstance(ret, Iterable))  # TODO: 可迭代对象 True
print(isinstance(ret, Iterator))  # TODO: 迭代器对象 True
print('=' * 40)

"""
2019/11/21 23:10
"""


# TODO: 自定义迭代器

class MyCustomizeIter(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start

    # TODO: 可迭代对象
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.end:
            temp = self.index
            self.index += 1
            return temp
        else:
            raise StopIteration()


class MyCustomizeRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start

    # TODO: 创建可迭代对象
    def __iter__(self):
        # TODO: 返回一个迭代器对象
        return MyCustomizeIter(self.start, self.end)


# TODO: 初始化一个可迭代对象
my_ret = MyCustomizeRange(1, 10)
for x in my_ret:
    print(x)

# print('=' * 40)
#
# for y in my_ret:
#     print(y)

print('=' * 40)

# TODO: 使用iter()方法获取可迭代对象的迭代器
"""
使用iter(x)方法将可迭代对象转化为迭代器
"""
ret_iterator = iter(my_ret)
# for y in ret_iterator:
#     print(y)

while True:
    try:
        y = ret_iterator.__next__()
        print(y)
    except StopIteration:
        break
