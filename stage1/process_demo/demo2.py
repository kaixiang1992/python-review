"""
2019/12/08 14:55
141.【Python多任务编程】join阻塞方法
"""

"""
父进程会等待子进程执行完毕后在退出：
如果在父进程中执行完所有代码后，还有子进程在执行，那么父进程会等待子进程执行完所有代码后再退出。

Process对象的join方法：
使用Process创建子进程，调用start方法后，父子进程会在各自的进程中不断的执行代码。
有时候如果想等待子进程执行完毕后再执行下面的代码，那么这时候调用join方法。
"""

from multiprocessing import Process
import time


def zhiliao():
    print('===子进程开始===')
    for x in range(0, 5):
        print('子进程： %s' % x)
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=zhiliao)
    p.start()

    print('主进程...')
    p.join()

    # print('执行主进程代码...')
    # for x in range(0, 6):
    #     print('主进程： %s' % x)
    #     time.sleep(1)

    print('所有子进程代码执行')
