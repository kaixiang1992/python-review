"""
2019/11/18 22:57
108.【Python知识补充】property装饰器
"""

# TODO: property装饰器
"""
有些时候你给一个类的某个属性设置变量的时候，可能除了设置变量，还要做一些其它的事情。
或者你在读取某个值的时候，想在返回值之前做点其他的事情，那么你可以使用property装饰器来完成。
"""


def cancel_schedule():
    print('取消各类事件调度...')


class Plane(object):

    def __init__(self):
        self._alive = True  # TODO: 飞机存活状态
        self._score = 0  # TODO: 游戏分数

    @property
    def alive(self):
        print('获取_alive参数: %s...' % self._alive)
        if not self._alive:  # TODO: 飞机被击落
            self.cancel_schedule()  # TODO: 取消事件调度
        return self._alive

    @alive.setter
    def alive(self, value):
        print('设置_alive参数: %s...' % value)
        self._alive = value
        if not value:  # TODO: 飞机被击落
            self.die_action()

    def cancel_schedule(self):
        print('取消各类事件调度...')

    def die_action(self):
        print('飞机击落状态切换...')

    @property
    def score(self):
        print('获取游戏分数: %d 分' % self._score)
        return self._score

    @score.setter
    def score(self, value):
        print('设置游戏分数: %d 分' % value)
        self._score = value
        self.update_standings(value)  # TODO: 更新游戏排行榜

    def update_standings(self, value):
        print('排行榜更新分数至: %d 分' % value)


plane = Plane()

# TODO: 是否被击中
hit = True
if hit:
    plane.alive = False  # TODO: setter
    temp = plane.alive  # TODO: getter
    plane.score = 200  # TODO: setter
    plane.score = 300  # TODO: setter
    plane.score = 400  # TODO: setter
    score = plane.score  # TODO: getter
