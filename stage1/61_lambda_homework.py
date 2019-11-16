"""
2019/11/16 13:15
61.【Python函数】函数式编程作业讲解
"""
from functools import reduce

# TODO: 1.使用filter函数过滤掉小于3的数

a = [1, 2, 3, 4, 5, 6, 7, 8]
# result_a = filter(lambda x: True if x > 3 else False, a)
result_a = filter(lambda x: x > 3, a)
# TODO: [4, 5, 6, 7, 8]
print(list(result_a))
print('=' * 50)

# TODO: 2.使用map函数将以下数组中所有的数扩大10倍

b = [1, 2, 3, 4, 5, 6, 7, 8]
result_b = map(lambda x: x * 10, b)
# TODO: [10, 20, 30, 40, 50, 60, 70, 80]
print(list(result_b))
print('=' * 50)

# TODO: 3.使用reduce函数求以下列表中数值之和

c = [1, 2, 3, 4, 5, 6, 7, 8]
result_c = reduce(lambda x, y: x + y, c)
print(result_c)
