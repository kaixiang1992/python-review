""""
2019/12/10 22:53
149.【多线程】多线程概念和threading模块介绍(线程)
"""

"""
threadingz模块介绍
threading模块是python中专门提供用来做多线程编程的模块。threading模块中最常用的类是Thread
"""

import threading
import time


# TODO: 统计函数执行时间
def time_total(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        diff = float(end - start)
        print('执行时间: %.2fs' % diff)

    return wrapper


@time_total
def coding():
    for x in range(0, 3):
        print('正在编码: %s' % x)
        time.sleep(1)


@time_total
def drawing():
    for x in range(0, 3):
        print('正在画画: %s' % x)
        time.sleep(1)


# TODO: 传统方式调用
# @time_total
# def main():
#     coding()
#     drawing()
#
#
# if __name__ == '__main__':
#     main()    # TODO: 执行时间: 6.00s


# TODO: 多线程模式
def multi_thread():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()


if __name__ == '__main__':
    multi_thread()
