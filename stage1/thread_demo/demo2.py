"""
2019/12/12 22:11
150.【多线程】使用Thread类创建多线程(线程)
"""

"""
查看线程数:
使用`threading.enumerate()`函数可以看到当前线程的数量.

查看当前线程的名字:
使用`threading.currentThread()`可以看到当前线程的信息.

继承自`threading.Thread`类:
为了让线程代码更好的封装。可以使用threading模块下的Thread类，继承自这个类，
然后实现run方法，线程就会自动运行run方法中的代码。
"""

import threading
import time


class codingThread(threading.Thread):
    def run(self):
        for x in range(0, 3):
            print('正在写代码%s' % threading.currentThread())
            time.sleep(1)


class drawingThread(threading.Thread):
    def run(self):
        for x in range(0, 3):
            print('正在画画%s' % threading.currentThread())
            time.sleep(1)


if __name__ == '__main__':
    coding = codingThread()
    drawing = drawingThread()

    coding.start()
    drawing.start()

    # TODO: [<_MainThread(MainThread, started 13016)>, <codingThread(Thread-1, started 3300)>, <drawingThread(
    #  Thread-2, started 8452)>]
    print('当前总线程数量： %s' % threading.enumerate())




