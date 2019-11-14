"""
2019/11/14 22:08
58.【Python函数】sort方法的高级用法

sort方法: 会改变原来列表的方法
sorted函数：不会改变原来列表的顺序，而是返回一个排序后的新的列表
"""
from functools import cmp_to_key

# TODO: 1.sort函数基本使用

print('sort函数基本使用排序列表')
numbers = [9, 11, 27, 16, 7, 13, 31, 49, 22]
numbers.sort()
# TODO: [7, 9, 11, 13, 16, 22, 27, 31, 49]
print(numbers)
print('=' * 40)

# TODO: 2.sort函数排序字典

print('sort函数排序字典')
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


def cmp(a, b):
    # TODO: 如果返回的是一个大于0的值，那么 a>b
    # TODO: 如果返回的是一个小于0的值，那么 a<b
    # TODO: 如果返回的是一个等于0的值，那么 a=b
    if a.get('age') > b.get('age'):
        return 1
    elif a.get('age') < b.get('age'):
        return -1
    else:
        if a.get('name') > b.get('name'):
            return 1
        else:
            return -1


persons.sort(key=cmp_to_key(cmp))
# TODO: [{'name': 'lisi', 'age': 18}, {'name': 'wangwu', 'age': 20}, {'name': 'zhangsan', 'age': 20}]
print(persons)
print('=' * 40)

# TODO: 3.sorted函数排序字典

print('sorted函数排序字典')

fruits = [
    {
        'name': 'apple',
        'price': 10
    },
    {
        'name': 'pear',
        'price': 5
    },
    {
        'name': 'orange',
        'price': 6
    }
]


def cmp2(a, b):
    if a.get('price') > b.get('price'):
        return 1
    elif a.get('price') < b.get('price'):
        return -1
    else:
        if a.get('name') > b.get('name'):
            return 1
        else:
            return -1


new_fruits = sorted(fruits, key=cmp_to_key(cmp2))
# TODO: [{'name': 'pear', 'price': 5}, {'name': 'orange', 'price': 6}, {'name': 'apple', 'price': 10}]
print(new_fruits)
# TODO: [{'name': 'apple', 'price': 10}, {'name': 'pear', 'price': 5}, {'name': 'orange', 'price': 6}]
print(fruits)
