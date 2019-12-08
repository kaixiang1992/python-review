"""
2019/12/08 20:54
145.【Python多任务编程】父子进程数据共享问题(进程)
"""

"""
进程间数据不共享：
在一个程序中，如果创建了一个子进程，那么这个子进程会拷贝一份当前进程所有的资源(变量，函数，类等)作为子进程的运行环境。
也就是说，子进程中的变量可能跟父进程一样，但其实是另外一个内存区域了。他们之间的数据是不共享的。
"""

from multiprocessing import Process

AGE = 1


def hello():
    print('hello world!')


def zhiliao(names):
    global AGE
    AGE += 1
    names.append('ketang')
    print('=====子进程开始=====')
    print('AGE: %s, AGE id: %s' % (AGE, id(AGE)))
    print('names: %s' % names)
    print(id(hello))
    print('=====子进程结束=====')


if __name__ == '__main__':
    names = ['zhiliao']
    p = Process(target=zhiliao, args=(names,))
    p.start()
    p.join()

    print('*****主进程开始*****')
    print('AGE: %s, AGE id: %s' % (AGE, id(AGE)))
    print('names: %s' % names)
    print(id(hello))
