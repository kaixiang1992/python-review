"""
2019/11/14 23:30
59.【Python函数】lambda表达式
"""
from functools import cmp_to_key

# TODO: 1.lambda表达式基础使用

print('lambda表达式基础使用')
persons = [
    {
        'name': 'zhangsan',
        'age': 20
    },
    {
        'name': 'lisi',
        'age': 18
    },
    {
        'name': 'wangwu',
        'age': 20
    }
]

# TODO: 使用cmp_to_key实现
# def my_cmp(a, b):
#     if a.get('age') > b.get('age'):
#         return 1
#     elif a.get('age') < b.get('age'):
#         return -1
#     else:
#         return 0
#
#
# persons.sort(key=cmp_to_key(my_cmp))
# # TODO: [{'name': 'lisi', 'age': 18}, {'name': 'zhangsan', 'age': 20}, {'name': 'wangwu', 'age': 20}]
# print(persons)

# TODO: 使用lambda实现
persons.sort(key=lambda x: x.get('age'))
print(persons)
print('=' * 50)

# TODO: 2.lambda表达式实现加减乘除运算

print('lambda表达式实现加减乘除运算')


def calculator(x, y, func):
    result = func(x, y)
    return result


a = 10
b = 5

# TODO: 加法
result1 = calculator(a, b, lambda x, y: x + y)
# 加法：15
print('加法:{}'.format(result1))

# TODO: 减法
result2 = calculator(a, b, lambda x, y: x - y)
# 减法:5
print('减法:{}'.format(result2))

# TODO: 乘法
result3 = calculator(a, b, lambda x, y: x * y)
# 乘法:50
print('乘法:{}'.format(result3))

# TODO: 除法
result4 = calculator(a, b, lambda x, y: x / y)
# 除法:2.0
print('除法:{}'.format(result4))
