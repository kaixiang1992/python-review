"""
2019/12/15 14:31
154.【多线程】Queue线程安全队列讲解(线程)
"""

"""
Queue线程安全队列:
如果你是想把一些数据存储到某个队列中，那么Python内置了一个线程安全的模块叫做queue模块。Python中的queue模块中提供了同步的、
线程安全的队列类，包括FIFO（先进先出）队列Queue。这些队列都实现了锁原语（可以理解为原子操作，即要么不做，要么都做完），能够
在多线程中直接使用。可以使用队列来实现线程间的同步。

Queue相关函数操作：
1.初始化Queue(maxsize)：创建一个先进先出的队列。
2.qsize()：返回队列的大小。
3.empty()：判断队列是否为空。
4.full()：判断队列是否满了。
5.get()：从队列中取最后一个数据。
6.put()：将一个数据放到队列中。
"""

from queue import Queue
import threading
import time


def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(1)


def get_value(q):
    while True:
        print('当前线程：%s' % (threading.current_thread()))
        print(q.get())


def main():
    # TODO: 初始化消息队列
    q = Queue(4)

    t1 = threading.Thread(target=set_value, args=(q,))
    t2 = threading.Thread(target=get_value, args=(q,))

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
