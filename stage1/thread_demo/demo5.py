"""
2019/12/15 13:33
153.【多线程】Condition版生产者与消费者模式(线程)
"""

"""
Condition版的生产者与消费者模式:
Lock版本的生产者与消费者模式可以正常的运行。但是存在一个不足，在消费者中，总是通过while True死循环并且上锁的方式去判断钱够不够。
上锁是一个很耗费CPU资源的行为。因此这种方式不是最好的。还有一种更好的方式便是使用threading.Condition来实现。

threading.Condition可以在没有数据的时候处于阻塞等待状态。一旦有合适的数据了，还可以使用notify相关的函数来通知其他处于等待状态
的线程。这样就可以不用做一些无用的上锁和解锁的操作。可以提高程序的性能。
threading.Condition常用相关的函数介绍：
1.acquire：上锁。
2.release：解锁。
3.wait：将当前线程处于等待状态，并且会释放锁。可以被其他线程使用notify和notify_all函数唤醒。
    被唤醒后会继续等待上锁，上锁后继续执行下面的代码。
4.notify：通知某个正在等待的线程，默认是第1个等待的线程。
5.notify_all：通知所有正在等待的线程。notify和notify_all不会释放锁。并且需要在release之前调用。
"""

import threading
import random
import time

gMoney = 1000  # TODO: 初始化金额
gCondition = threading.Condition()  # TODO: Condition函数
gTimes = 0  # TODO: 总生产次数


# TODO: 生产者
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100, 1000)  # TODO: 随机生成100-1000整数金额
            gCondition.acquire()  # TODO: 开始上锁
            if gTimes > 10:
                gCondition.release()  # TODO: 超过最大生产次数释放锁
                break
            gMoney += money
            print('%s生产者，生产了%s元，剩余%s元' % (threading.current_thread(), money, gMoney))
            gTimes += 1
            # TODO: 通知所有正在等待的线程并且在release之前调用
            gCondition.notify_all()
            gCondition.release()  # TODO: 生产完毕释放锁
            time.sleep(1)


# TODO: 消费者
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)   # TODO: 随机消费100-1000元
            gCondition.acquire()    # TODO: 开始上锁
            while money > gMoney:
                if gTimes > 10:
                    print('生产次数已超上线，当前消费余额不足，结束线程...')
                    gCondition.release()
                    return
                print('准备消费%s元，当前余额%s元，余额不足......' % (money, gMoney))
                # TODO: 将当前线程处于等待状态，且释放锁。
                gCondition.wait()
            gMoney -= money
            print('%s消费者，消费了%s元，剩余%s元' % (threading.current_thread(), money, gMoney))
            gCondition.release()    # TODO: 消费完成释放锁
            time.sleep(1)


def main():
    # TODO: 3个消费者
    for x in range(0, 3):
        t = Consumer(name='%s' % (x,))
        t.start()

    # TODO: 5个生产者
    for x in range(0, 5):
        t = Producer(name='%s' % (x, ))
        t.start()


if __name__ == '__main__':
    main()
