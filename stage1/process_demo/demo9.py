""""
2019/12/10 20:58
148.【Python多任务编程】Pool进程间通信(进程)
"""

"""
Pool进程间通信:
使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，而不是multiprocessing.Queue()，否则会报错

RuntimeError: Queue objects should only be shared between processes through inheritance
"""
from multiprocessing import Pool, Manager
import os


# TODO: 写
def write(q):
    for x in ['m1', 'm2', 'm3']:
        q.put(x)
        print('子进程%s，存入数据: %s' % (os.getpid(), x))


# TODO: 读
def read(q):
    while True:
        try:
            # TODO: 默认阻塞, block = False不阻塞，没有消息时立即抛出异常
            msg = q.get(block=False)
            print('子进程%s，读取数据: %s' % (os.getpid(), msg))
        except Exception as error:
            print(error)
            break


if __name__ == '__main__':
    print('主进程....')
    q = Manager().Queue(3)
    pool = Pool(2)
    # TODO:同步执行写的子进程
    pool.apply(func=write, args=(q,))
    # TODO: 同步执行读的子进程
    pool.apply(func=read, args=(q,))

    # TODO: 关闭进程池，不再添加其他的进程
    pool.close()

    pool.join()
    print('所有子进程代码执行完毕...')
