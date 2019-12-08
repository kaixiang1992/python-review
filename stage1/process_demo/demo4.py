"""
2019/12/08 15:51
143.【Python多任务编程】进程池详解(进程)
"""

"""
进程池：
multiprocessing模块中有一个类`Pool`, 这个类相当于一个池，专门用来存储进程的。
Pool的__init__可以传递一个参数，这个参数指定这个进程池同一时刻最多只能拥有多少个进程。
并且，在使用进程池，父进程不会等待子进程池中的子进程执行完毕后退出，而是当父进程中的代
码执行完毕后会立即退出。

主进程把子进程添加到进程池后，不会等待进程池中其他子进程都执行完毕后再退出，
而是当主进程代码执行完毕后会立刻退出，因此如果这个地方没有join，那么子进程
将得不到执行
"""

from multiprocessing import Pool
import os
import time


def zhiliao(num):
    for x in range(0, 5):
        print('子进程ID： %s, num: %s, x: %s' % (os.getpid(), num, x))
        time.sleep(1)


if __name__ == '__main__':
    # TODO: 这个池子同一时刻最多只能有3个进程
    pool = Pool(3)
    for x in range(0, 10):
        pool.apply_async(zhiliao, args=(x,))

    # TODO: 关闭进程池，不能再添加新进程了
    pool.close()

    print('主进程...')
    """
    主进程把子进程添加到进程池后，不会等待进程池中其他子进程都执行完毕后再退出，
    而是当主进程代码执行完毕后会立刻退出，因此如果这个地方没有join，那么子进程
    将得不到执行
    """
    pool.join()
    print('所有子进程执行完毕...')
