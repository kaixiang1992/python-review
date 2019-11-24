"""
2019/11/24 16:27
114.【Python生成器】生成器的基本使用
"""

# TODO: 1.解决打印1-1亿的问题

# TODO: 普通生成模式

# num_list = [x for x in range(1, 100000000)]
# for num in num_list:
#     print(num)


# TODO: 生成器模式

# num_gen = (x for x in range(1, 100000000))
# for num in num_gen:
#     print(num)


# TODO: 2.自己写生成器
"""
next函数可以迭代生成器的返回值
"""


def my_gen():
    yield 1
    yield 2
    yield 3


ret = my_gen()
print(next(ret))
print(ret.__next__())
print(next(ret))
print('=' * 50)


def MyRange(start, end):
    index = start
    while index <= end:
        yield index
        index += 1


my_range = MyRange(1, 10)
# for num in my_range:
#     print(num)

while True:
    try:
        print('value is {}'.format(next(my_range)))
    except StopIteration as error:
        break
