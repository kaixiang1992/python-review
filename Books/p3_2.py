"""
2020/01/17 00:15
* Page: 17 5次猜1-10随机整数猜数字游戏
"""

# random.randint(1, 10)： 随机生成1-10的整数

import random

successnum = random.randint(1, 10)  # TODO: 随机生成1-10的整数
print('本轮幸运数字：%d' %(successnum, ))
useript = input('请输入幸运数字：')
guess = int(useript)  # TODO: 用户猜测输入整数
times = 1   # TODO: 猜的次数

# TODO: 当输入数字不等于幸运数字且参数次数小于5，便一直参与游戏
while guess != successnum and times < 5:
    if guess > successnum:
        print('大了大了')
    else:
        print('小了小了')
    temp = input('继续输入幸运数字：')
    guess = int(temp)
    times += 1

# TODO: 猜中幸运数字且游戏次数小于5次
print('参与游戏次数：%d' % (times, ))
if guess == successnum and times < 5:
    print('猜中了，也没有奖励哦。。。')
else:
    print('五次机会都没猜中，不和你玩了。。。')