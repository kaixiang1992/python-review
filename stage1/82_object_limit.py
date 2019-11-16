"""
2019/11/16 16:52
82.【Python面向对象】访问限制（受保护和私有）
"""

# TODO: 1.受保护的属性或者方法
"""
有时候在类中的属性或者方法不想被外界调用，但还是可以被外界调用，
那么就叫做受保护的属性或者方法。受保护的属性或者方法，使用一个
下划线_开头.
"""


class Women(object):
    def __init__(self, age):
        # TODO: 受保护的属性
        self._age = age

    # @property
    # def age(self):
    #     return self._age


women = Women(19)
# TODO: 可以打印_age, 但违背开发者意愿
print(women._age)
print('=' * 50)

# TODO: 2.私有属性和方法
"""
有时候在类中的属性或者方法不想被外界调用，那么就可以使用定义成
私有属性或者私有方法。私有属性或者私有方法使用两个下划线__开头.

直接访问私有属性将抛出异常：
AttributeError: '类名' object has no attribute '__属性名|方法名'

私有属性或者方法不是说100%不能被访问，使用对象._类名__私有属性名来访问,
但这样访问是不推荐的(写bug的吗?).
例：print(account1._Account__password)  #TODO: admin123
"""


class Account(object):

    def __init__(self, a_id, password):
        # TODO: 公有属性用户id
        self.a_id = a_id
        # TODO: 私有属性用户密码信息
        self.__password = password

    def __account_list(self):
        print('调用私有方法...')
        return [1, 11, 101, 22]

    def get_account_list(self, password):
        if password == self.__password:
            return self.__account_list()
        else:
            return None

account1 = Account('123', 'admin123')
account1.get_account_list('admin123')

# TODO: 访问私有属性
print(account1._Account__password)  #TODO: admin123
