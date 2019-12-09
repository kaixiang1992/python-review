"""
2019/12/09 22:30
146.【Python多任务编程】Queue消息队列(进程)
"""

"""
Queue的常用方法:
1.Queue(n)：初始化一个消息队列，并指定这个队列中最多能够容纳多少条消息。
2.put(obj,[block[,timeout]])：推入一条消息到这个队列中。
    block=True: 默认是阻塞的，也就是说如果这个消息队列中已经满了，那么会会一直等待，将这个消息添加到消息队列中。
    timeout(秒): 可以指定这个阻塞最长的时间，如果超过这个时间还是满的，就会抛出异常。
3.put_nowait() ：非阻塞的推入一条消息，如果这个队列已经满了，那么会立马抛出异常。
4.qsize()：获取这个消息队列消息的数量。
5.full()：判断这个消息队列是否满了。
6.empty()：判断这个消息队列是否空了。
7.get([block[,timeout]])：获取队列中的一条消息，然后将其从队列中移除，
    block: 默认为True。如果设置block为False，那么如果没值，会立马抛出异常。
    timeout: 指定如果多久没有获取到值后会抛出异常。
"""

from multiprocessing import Queue

"""
Queue可以指定maxsize的值
以后这个队列中只能装maxsize个值
如果不指定，那么就是-1
-1意味着可以装任意多个消息，直到你的内存满了
"""
q = Queue(3)

# TODO: put方法推入一条任意数据类型的消息到队列中
q.put([1, 2, 3])
q.put('m2')
q.put('m3')

# TODO: qsize()方法获取这个消息队列的数量
print('qsize(): %s' % q.qsize())

# TODO: full()方法判断这个消息队列是否满了
print('full(): %s' % q.full())

# TODO: empty()方法判断这个消息队列是否为空
print('empty(): %s' % q.empty())

# TODO: put方法默认是阻塞的方式
# TODO: 如果消息队列已经满了，那么会阻塞在这个地方，直到这个消息队列没有满为止
# TODO: block参数：可以设置为False，如果为False，那么意味着不会阻塞
# TODO: 如果消息队列满了，那么会立马抛出一个异常
# TODO: timeout参数(秒)：指定阻塞的最长时间。如果超过了这个时间就不再阻塞，而是抛出一个异常。

# TODO: 不阻塞如果消息队列满了，立马抛出一个异常
# q.put('m4', block=False)

# TODO: 阻塞模式，超时2秒后就抛出异常
# q.put('m4', block=True, timeout=2)

# TODO: put_nowait: 非阻塞的推入一条消息，如果这个队列已经满了，那么会立马抛出异常
# TODO: 相当于执行q.put('m4', block=False)
# q.put_nowait('m4')
print('=====get=====')

# TODO: get方法：获取到的是第一个添加进去的值。先进先出。
# TODO: get方法：除了获取这个值外，还会把这个值从消息队列中删除掉
# TODO: block参数：默认是等于True，即以阻塞的方式获取值，如果这个队列中没有任何消息，
#  那么会阻塞到这个地方。
# TODO: 如果block=False，那么如果队列中没有值，就会立即抛出异常。
# TODO: timeout参数(秒)：指定阻塞的最长事件。如果超过了这个时间就不再阻塞，而是抛出一个异常

print(q.get())
print(q.get())
print(q.get())

# TODO: block参数：默认是等于True，即以阻塞的方式获取值，如果这个队列中没有任何消息，那么会阻塞到这个地方。
# print(q.get())
# TODO: block=False，那么如果队列中没有值，就会立即抛出异常。
# print(q.get(block=False))
# TODO: timeout参数(秒)：指定阻塞的最长事件。如果超过了这个时间就不再阻塞，而是抛出一个异常
print(q.get(block=True, timeout=2))
