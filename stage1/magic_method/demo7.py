"""
2019/12/3 23:00
135.【Python魔术方法】创建属于自己的序列
"""

"""
序列容器的魔术方法：
1.__len__(self): 在使用len(obj)函数的时候会调用这个魔术方法.
2.__getitem__(self, key): 在使用下标操作`temp[key]`以及切片操作的时候会调用这个魔术方法.
3.__setitem__(self, key): 在给这个容器设置key和value的时候会调用这个魔术方法.
4.__delitem__(self, key): 在删除容器中的某个key对应的这个值的时候会调用这个魔术方法.
5.__iter__(self): 在遍历这个容器的时候，会调用容器的这个方法，然后返回一个迭代器，再调用
    这个迭代器的__next__方法.
6.__reversed__(self): 在调用reversed(obj)函数的时候会调用这个方法.
"""


class CustomizeList(object):
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        # TODO: slice 数据类型
        # print(type(item))
        # slice(0, 2, None)
        # print(isinstance(item, slice))  # TODO: True

        # TODO: 只是为了介绍了解slice类型
        # if isinstance(item, slice):
        #     return self.values[item.start:item.stop:item.step]
        # else:
        #     return self.values[item]

        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)


customize_list = CustomizeList([1, 2, 3, 4])
# TODO: __len__
print('__len__...')
print(len(customize_list))

# TODO: __getitem__
print('__getitem__...')
print(customize_list[0:2])

# TODO: __setitem__
print('__setitem__...')
customize_list[0:2] = ['a', 'b']
print(customize_list[::])

# TODO: __delitem__
print('__delitem__...')
del customize_list[3]
print(customize_list[::])

# TODO: __iter__
print('__iter__...')
for x in customize_list:
    print(x)

# TODO: __reversed__
print('__reversed__...')
print(list(reversed(customize_list))[::])
