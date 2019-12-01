"""
2019/12/1 16:48
128.【Python内存管理】gc模块
"""

"""
gc模块常用函数:
gc.set_debug(flags):设置gc的debug日志，一般设置为gc.DEBUG_LEAK可以看到内存泄露的对象。
gc.collect(generation):执行垃圾回收。会将那些循环引用的对象给回收了。
    不传参数，默认使用2作为默认参数。
    传递参数说明：
    0：只回收第0代的垃圾对象
    1：回收第0代、第1代的对象
    2：回收第0代、第1代、第2代的对象。
gc.get_threshold():获取gc模块执行垃圾回收的阈值。
gc.set_threshold()：设置垃圾回收的阈值。
gc.get_count():获取自动执行垃圾回收的计数器。
    返回的是一个元祖。
    第0个是零代的垃圾对象的数量
    第1个是零代链表遍历的次数
    第2个是1代链表遍历的次数
"""

import gc


class Person(object):
    def __init__(self, name):
        self.name = name
        self.pointer = None

    # TODO: 析构函数
    def __del__(self):
        print('%s 被回收了...' % self.name)


# TODO: 获取垃圾回收的阈值
# print(gc.get_threshold())  # TODO: (700, 10, 10)
# TODO: 设置垃圾回收的阈值
# gc.set_threshold(500)
# print(gc.get_threshold())  # TODO: (500, 10, 10)

# TODO: 设置gc的debug日志，可以看到内存泄露的对象
gc.set_debug(gc.DEBUG_LEAK)

while True:
    # TODO: 获取垃圾回收的计数器
    print(gc.get_count())

    p1 = Person('p1')
    p2 = Person('p2')

    # TODO: 产生循环引用
    p1.pointer = p2
    p2.pointer = p1

    del p1
    del p2

    a = input('随便输入点啥：...')
    # TODO: 回收第0代垃圾对象
    # gc.collect(0)

    # TODO: 回收第0代、第1代垃圾对象
    # gc.collect(1)

    # TODO: 回收第0代、第1代、第2代垃圾对象
    gc.collect(2)
