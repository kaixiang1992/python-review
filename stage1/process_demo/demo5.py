"""
2019/12/08 16:29
144.【Python多任务编程】进程池补充
"""

"""
`apply_async`相当于并联的方式执行(同一时刻可以执行多个任务).
`apply`相当于串联的方式执行(同一时刻只能执行一个任务，并且只能等待前面的任务执行完后才能执行后面的任务).
"""

from multiprocessing import Pool
import os
import time


def zhiliao(num):
    for y in range(0, 5):
        print('子进程ID：%s，num: %s, x: %s' % (os.getpid(), num, y))
        time.sleep(1)


if __name__ == '__main__':
    pool = Pool(3)
    for x in range(0, 10):
        pool.apply(zhiliao, args=(x,))

    pool.close()
    print('主进程...')
    pool.join()
    print('所有子进程代码执行完毕...')
