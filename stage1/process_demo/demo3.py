"""
2019/12/08 15:16
142.【Python多任务编程】使用类的方式创建子进程(进程)
"""

"""
使用类的方式创建子进程：
有些时候，你想以类的形式定义子进程的代码。那么你可以自定义一个类，让他继承自`Process`,
然后在这个类中实现run方法，以后这个子进程在执行的时候就会调用run方法中的代码。
"""

from multiprocessing import Process
import os


class zhiliao(Process):
    def run(self):
        print('子进程ID： %s' % os.getpid())
        print('父进程ID： %s' % os.getppid())
        for x in range(0, 5):
            print('子进程： %s' % x)


if __name__ == '__main__':
    p = zhiliao()
    p.start()

    print('主进程ID: %s' % os.getpid())

    p.join()
    print('所有子进程代码执行完毕...')
