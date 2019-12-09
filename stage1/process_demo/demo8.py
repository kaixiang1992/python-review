""""
2019/12/09 23:08
147.【Python多任务编程】Process进程间通信(进程)
"""

"""
Process进程间通信
"""

from multiprocessing import Process, Queue
import os


def write(q):
    for x in ['m1', 'm2', 'm3']:
        # TODO: 以阻塞模式写入数据
        q.put(x)
        print('q ID: %s, 子进程%s，写入数据: %s' % (id(q), os.getpid(), x))


def read(q):
    while True:
        try:
            # TODO: 以非阻塞模式读取消息，如果消息队列中没有值，就会立即抛出异常
            msg = q.get(block=False)
            print('q ID: %s, 子进程%s, 读取数据: %s' % (id(q), os.getpid(), msg))
        except Exception as error:
            print(error)
            break


if __name__ == '__main__':
    q = Queue(3)
    print('主进程')

    # TODO: 写入
    pw = Process(target=write, args=(q,))
    # TODO: 读取
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    # TODO: 子进程代码执行完毕后，在继续执行主进程代码
    pr.join()

    print('所有子进程代码执行完毕...')
