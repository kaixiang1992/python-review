"""
2019/12/23 23:42
162.【正则表达式】开始结束和或语法
"""
import re

# TODO: 1. ^托字号: 表示以...开始
"""
如果是在中括号中，那么代表取反操作.
"""

text1 = 'hello'
ret_text1 = re.match('^h', text1)
print('^托字号: 表示以...开始...')
print(ret_text1.group())

# TODO: 2.$ 表示以...结束

email = 'hynever@163.com'
ret_email = re.match('\w+@163\.com$', email)
print('$ 表示以...结束...')
print(ret_email.group())

# TODO: 3.| 匹配多个表达式或者字符串

url = 'https'
ret_url = re.match('(http|https|ftp)$', url)
print('| 匹配多个表达式或者字符串...')
print(ret_url.group())

# TODO: 4.贪婪模式和非贪婪模式
"""
贪婪模式：正则表达式会匹配尽量多的字符。默认是贪婪模式。
非贪婪模式：正则表达式会尽量少的匹配字符。
"""

text2 = '01234567'
ret_text2 = re.match('\d+?', text2)
print('贪婪模式和非贪婪模式...')
print(ret_text2.group())

h1 = '<h1>标题</h1>'
ret_h1 = re.match('<.*?>', h1)
print('贪婪模式和非贪婪模式...')
print(ret_h1.group())

# TODO: 5.匹配0-100之间的数字
# TODO: 可以出现的：1，2，3，10，100，99
# TODO: 有三种情况：1，99，100
# TODO: 不可以出现的：09，101

num = '1'
ret_num = re.match('([1-9]?\d$|100$)', num)
print('匹配0-100之间的数字...')
print(ret_num.group())
