"""
2019/11/17 18:04
99.【Python模块和包】__all__变量的作用
"""

import sys

# TODO: __all__
"""
1.如果是在模块中写了这个变量，将控制from 模块名字 import * 的行为.
2.如果是在__init__.py文件中有这个变量，那么将控制着 from 包 import * 的行为.
"""

print(sys.path)

from zhiliao import *

print(GLOBAL_STR)
greet()
# TODO: NameError: name 'Person' is not defined
# p = Person()