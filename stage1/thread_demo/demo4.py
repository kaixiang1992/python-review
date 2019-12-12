"""
2019/12/12 23:06
152.【多线程】Lock版生产者和消费者模式(线程)
"""

"""
Lock版本生产者和消费者模式:
生产者和消费者模式是多线程开发中经常见到的一种模式。
生产者的线程专门用来生产一些数据，然后存放到一个中间的变量中。
消费者再从这个中间的变量中取出数据进行消费。

但是因为要使用中间变量，中间变量经常是一些全局变量，因此需要使用锁
来保证数据完整性。以下是使用threading.Lock锁实现的“生产者与消费者模式”
"""
import threading
import random
import time

gMoney = 1000  # TODO: 初始化金额
gLock = threading.Lock()  # TODO: 全局锁
gTime = 0  # TODO: 全局生产次数


# TODO: 生产者
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            money = random.randint(0, 1000)  # TODO: 随机产生0-1000的整数
            gLock.acquire()  # TODO: 加锁
            if gTime > 10:  # TODO: 如果生产次数大于10次，就不再生产了
                gLock.release()  # TODO: 释放锁
                break
            gMoney += money
            gTime += 1
            print('%s线程生产了%s元，剩余%s元' % (threading.currentThread(), money, gMoney))
            gLock.release()  # TODO: 释放锁
            time.sleep(1)


# TODO: 消费者
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(0, 1000)  # TODO: 随机产生0-1000的整数
            gLock.acquire()  # TODO: 加锁
            if gMoney > money:  # TODO: 余额大于消费额
                gMoney -= money
                print('%s线程消费了%s元，剩余%s元' % (threading.currentThread(), money, gMoney))
            else:
                # TODO: 余额不足且消费大于10次，就不再消费
                if gTime > 10:
                    print('生产次数: %d, 余额不足，不再消费...' % gTime)
                    gLock.release()  # TODO: 释放锁
                    break
                print('%s线程准备消费%s元，剩余%s元，余额不足!...' % (threading.currentThread(), money, gMoney))
            gLock.release()  # TODO: 释放锁
            time.sleep(1)


def main():
    # TODO: 3个消费者线程
    for x in range(0, 3):
        consumer = Consumer(name='消费者线程%d' % x)
        consumer.start()

    # TODO: 5个生产者线程
    for x in range(0, 5):
        producer = Producer(name='生产者线程%d' %x)
        producer.start()


if __name__ == '__main__':
    main()
