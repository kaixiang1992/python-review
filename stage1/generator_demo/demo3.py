"""
2019/11/24 23:29
116.【Python生成器】生成器小案例
"""

# TODO: 1.斐波那契数列
"""
斐波拉契数列的算法：除第一个和第二个数以外，任意一个数都可由前两个数相加得到：
1,1,2,3,5,8,13,21,34,55...
a,b
  c
"""


def fib(count):
    index = 0
    a, b = 0, 1
    while index < count:
        c = b
        yield c
        b = a + b
        a = c
        index += 1


fib_ret = fib(10)
while True:
    try:
        print(next(fib_ret))
    except Exception as error:
        break

print('斐波那契数列 完毕....')
print('=' * 40)


# TODO: 2.用yiled做多任务切换

def qq_music(time):
    played_time = 0
    while played_time <= time:
        print('QQ音乐已播放%d分钟' % played_time)
        played_time += 1
        yield None


def youku_movie(time):
    played_time = 0
    while played_time <= time:
        print('优酷视频已播放%d分钟' % played_time)
        yield None
        played_time += 1


def main():
    music = qq_music(110)
    movie = youku_movie(120)
    music_end = False
    movie_end = False
    while True:
        try:
            next(music)
        except StopIteration:
            music_end = True

        try:
            next(movie)
        except StopIteration:
            movie_end = True

        if music_end and movie_end:
            break


if __name__ == '__main__':
    main()
