"""
2019/11/25 21:58
117.【Python装饰器】闭包及其使用
"""

# TODO: 1.什么是闭包
"""
如果在一个函数中，定义了另外一个函数，并且那个函数使用了外面函数的变量，并且外面
函数返回了里面这个函数的引用，那么称为里面的这个函数为闭包。
"""
print('什么是闭包....')


def greet(name):
    def say_hello():
        print('hello, my name is %s' % name)

    print(id(say_hello))
    return say_hello


ret = greet('zhiliao')
print(id(ret))
ret()
print('=' * 50)


# TODO: 2.用闭包完成一个计算器

def calculator(option):
    if option == '+':
        def add(x, y):
            return x + y

        print(id(add))
        return add
    elif option == '-':
        def minus(x, y):
            return x - y

        print(id(minus))
        return minus
    elif option == '*':
        def multiply(x, y):
            return x * y

        print(id(multiply))
        return multiply
    elif option == '/':
        def divide(x, y):
            return x / y

        print(id(divide))
        return divide
    else:
        raise SyntaxError('不支持该类型')


# TODO: 加法
add_func = calculator('+')
print(id(add_func))
print('2 + 5 = {}'.format(add_func(2, 5)))
print('12 + 15 = {}'.format(add_func(12, 15)))

# TODO: 减法
minus_func = calculator('-')
print(id(minus_func))
print('1 - 5 = {}'.format(minus_func(1, 5)))
print('10 - 1 = {}'.format(minus_func(10, 1)))

# TODO: 乘法
multiply_func = calculator('*')
print(id(multiply_func))
print('4 * 5 = {}'.format(multiply_func(4, 5)))
print('0.5 * 50 = {}'.format(multiply_func(0.5, 50)))

# TODO: 除法
divide_func = calculator('/')
print(id(divide_func))
print('50 / 10 = {}'.format(divide_func(50, 10)))
print('-5 / -5 = {}'.format(divide_func(-5, -5)))

# TODO: 不支持类型
# other_func = calculator('**')
print('=' * 50)

# TODO: 2.nonlocal关键字
"""
如果想在闭包中修改外面函数的变量，这时候应该使用nonlocal关键字，
来把这个变量标识为外面函数的变量。
"""
print('nonlocal关键字....')


def person(age):
    def say_hello():
        nonlocal age
        age += 1
        print('我今年虚岁：%d' % age)

    return say_hello


p = person(18)
p()
