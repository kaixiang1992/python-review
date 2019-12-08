"""
2019/12/08 14:28
140.【Python多任务编程】multiprocessing多进程编程
"""

"""
multiprocessing模块介绍：
multiprocessing提供了一个Process类创建进程.

获取进程号：
os模块：
getpid(): 获取当前进程的进程号
getppid(): 这个进程的父进程的进程号
"""

from multiprocessing import Process
import os


def zhiliao():
    print('===子进程开始===')
    print('zhiliao process')
    print('子进程ID： %s' % os.getpid())
    print('父进程ID： %s' % os.getppid())
    print('===子进程结束===')

# p = Process(target=zhiliao)
# p.start()

if __name__ == '__main__':
    p = Process(target=zhiliao)
    p.start()
    print('主进程ID: %s' % os.getpid())
