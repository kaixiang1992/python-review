"""
2019/12/6 23:21
137.【Python魔术方法】with语句魔术方法
"""

"""
with语句魔术方法，会话管理：
通过控制__enter__(self)以及__exit__(self, exception_type, exception_value, traceback)来定义一个代码块
被执行或者终止后会话管理器应该做什么。他可以被用来处理异常，清除工作或者做一些代码块执行完毕之后的日常工作。
如果代码执行成功，没有任何异常，那么exception_type, exception_value, traceback将会是None。
否则的话你可以选择处理这个异常或者直接交给用户处理。如果你不想处理这个异常的话，那么必须在__exit__在所有结
束之后返回True.会自动的吸收这个异常.
"""


class FileOpener(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.fq = None

    def __enter__(self):
        print('__enter__...')
        self.fq = open(self.filename, self.mode, encoding="utf8")
        return self.fq

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__...')
        self.fq.close()
        print(exc_type)  # TODO: None
        print(exc_val)  # TODO: None
        print(exc_tb)  # TODO: None
        # TODO: 用户想处理异常， return False
        # return False
        # TODO: 如果用户不想处理异常, return True
        return True

# TODO: 代码执行成功 exc_type, exc_val, exc_tb 都返回None
# print(exc_type)  # TODO: None
# print(exc_val)  # TODO: None
# print(exc_tb)  # TODO: None
# with FileOpener('./test.txt', 'w') as fp:
#     fp.write('hello world!')


with FileOpener('./test.txt', 'w') as fp:
    fp.write('hello world!')
    a = 1
    b = 0
    c = a / b