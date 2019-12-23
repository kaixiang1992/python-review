"""
2019/12/23 22:16
161.【正则表达式】常用匹配小案例
"""
import re

# TODO: 1.验证手机号码：手机号码的规则是以1开头，第二位可以是345879，后面那9位就可以随意了

phone = '18570631581'
ret_phone = re.match('1[345789]\d{9}', phone)
print('验证手机号码...')
print(ret_phone.group())

# TODO: 2.验证邮箱：邮箱的规则是邮箱名称是用字母、数字、下划线组成的，然后是@符号，后面就是域名了

email = 'hynever@163.com.cn'
ret_email = re.match('\w+@[a-z0-9]+\.\w+(\.\w+)?', email)
print('验证邮箱...')
print(ret_email.group())

# TODO: 3.验证URL：URL的规则是前面是http或者https或者是ftp然后再加上一个冒号，再加上一个斜杠，再后面就是可以出现任意非空白字符了

url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
ret_url = re.match(r'(http|https|ftp)://\S+', url)
print('验证URL...')
print(ret_url.group())

# TODO: 4.验证身份证：身份证的规则是，总共有18位，前面17位都是数字，后面一位可以是数字，也可以是小写的x，也可以是大写的X。

idcard = '31131118908123231X'
ret_idcard = re.match('\d{17}[\dxX]', idcard)
print('验证身份证...')
print(len(idcard))
print(ret_idcard.group())
