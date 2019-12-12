"""
2019/12/12 22:49
151.【多线程】多线程共享全局变量以及锁机制(线程)
"""

"""
多线程共享全局变量的问题:
多线程都是在同一个进程中运行的。因此在进程中的全局变量所有线程都是可共享的。
这就造成了一个问题，因为线程执行的顺序是无序的。有可能会造成数据错误。
"""

"""
锁机制:
为了解决使用全局变量的问题。`threading`提供了一个`Lock`类。这个类可以在某个
线程访问某个变量的时候加锁，其他线程此时就不会进来，直到当前线程处理完后，把
锁释放了，其他线程才能继续进来处理。
加锁: threading.Lock().acquire()
释放锁: threading.Lock().release()
"""
import threading
import time

VALUE = 0
gLOCK = threading.Lock()


def time_total(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        diff = end - start
        print('执行时间: %ds' % diff)

    return wrapper


@time_total
def add_value():
    global VALUE
    gLOCK.acquire()
    for x in range(0, 10000000):
        VALUE += 1
    gLOCK.release()
    print(VALUE)


def main():
    for x in range(0, 2):
        t = threading.Thread(target=add_value)
        t.start()


if __name__ == '__main__':
    main()
