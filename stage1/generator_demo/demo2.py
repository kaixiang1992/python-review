"""
2019/11/24 18:00
115.【Python生成器】send方法的用法
"""
"""
send方法和next方法类似，可以用来触发生成器的下一个yield,但是send不仅可以
触发下一个yield,还可以发送数据过去，作为yield表达式的值。
在第一次执行生成器代码的时候，send函数必须要传一个None过去，而next函数可
以不用传
报错异常：TypeError: can't send non-None value to a just-started generator
"""


def my_gen(start):
    while start < 10:
        """
        如果是通过next函数执行的yield
        那么yiele xxx永远返回None
        """
        temp = yield start
        print(temp)
        start += 1


ret = my_gen(1)

# print(next(ret))
# # TODO: 1
# print(next(ret))
# # TODO: None
# # TODO: 2
# print(ret.send('zhiliao'))
# # TODO: zhiliao
# # TODO: 3

print('全部由send函数调用...')
print(ret.send(None))
# TODO: 1
print(ret.send('zhiliao'))
# TODO: zhiliao
# TODO: 2
print(ret.send(None))
# TODO: None
# TODO: 3
