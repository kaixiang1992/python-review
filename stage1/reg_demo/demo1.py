"""
2019/12/19 22:09
159.【正则表达式】单字符匹配规则
"""

import re

# TODO: 1.匹配某个字符串

print('1.匹配某个字符串...')
str1 = 'hello'
ret1 = re.match('he', str1)
print(ret1.group())

# TODO: 2. 点(.)匹配任意的字符

print('2. 点(.)匹配任意的字符...')
str2 = 'ab'
ret2 = re.match('.', str2)
print(ret2.group())

# TODO: 2.1 点(.)不能匹配换行符
print('2.1 点(.)不能匹配换行符...')
# str3 = '\nhello'
# ret3 = re.match('.', str3)
# TODO: AttributeError: 'NoneType' object has no attribute 'group'
# print(ret3.group())

# TODO: 3. \d匹配任意的数字

print(r'3. \d匹配任意的数字...')
str4 = '123456'
ret4 = re.match('\d', str4)
print(ret4.group())

# TODO: 4. \D匹配任意的非数字

print(r'4. \D匹配任意的非数字...')
str5 = '+a1233456'
ret5 = re.match('\D', str5)
print(ret5.group())

# TODO: 5. \s匹配的是空白字符(\n换行符、\t制表符、\r和空格)

print(r'5. \s匹配的是空白字符(\n换行符、\t制表符、\r和空格)...')
str6 = '  '
ret6 = re.match('\s', str6)
print(ret6.group())

# TODO: 6.\w匹配的是a-z和A-Z以及数字和下划线

print(r'6.\w匹配的是a-z和A-Z以及数字和下划线...')
str7 = '_'
ret7 = re.match('\w', str7)
print(ret7.group())

# TODO: 7.\W匹配的是和\w相反的

print(r'7.\W匹配的是和\w相反的...')
str8 = '??'
ret8 = re.match('\W', str8)
print(ret8.group())

# TODO: 8.[]组合的方式，只要满足中括号中的某一项都算匹配成功

print(r'8.[]组合的方式，只要满足中括号中的某一项都算匹配成功...')
str9 = '0731-8888888avvav'
ret9 = re.match('[\d-]+', str9)
print(ret9.group())

# TODO: 8.1 中括号的形式来进行替代\d
print(r'8.1 中括号的形式来进行替代\d...')
str10 = '123456abbhjghg'
ret10 = re.match('[0-9]+', str10)
print(ret10.group())

# TODO: 8.2 中括号的形式来进行替代\D
print(r'8.2 中括号的形式来进行替代\D...')
str11 = 'abcd1234'
ret11 = re.match('[^0-9]+', str11)
print(ret11.group())

# TODO: 8.3 中括号的形式来进行替代\w
print(r'8.3 中括号的形式来进行替代\w...')
str12 = '1213abbvAZDG_===='
ret12 = re.match('[0-9a-zA-Z_]+', str12)
print(ret12.group())

# TODO: 8.4 中括号的形式来进行替代\W
print(r'8.4 中括号的形式来进行替代\W')
str13 = r'???..\\\///12123'
ret13 = re.match('[^0-9a-zA-Z_]+', str13)
print(ret13.group())
print('=' * 50)

"""
2019/12/19 22:58
160.【正则表达式】匹配多个字符
"""

# TODO: 9.* 可以匹配0或者任意多个字符。
"""
可有可无，多了不限
"""
print('9.* 可以匹配0或者任意多个字符。...')

# text = '0731-88888888'
text = '11  3344'
ret14 = re.match('\d*', text)
print(ret14.group())

# TODO: 10. +可以匹配1个或者多个字符。最少一个。
"""
最少一个，多了不限.
"""
print(r'10. +可以匹配1个或者多个字符。最少一个。...')
text2 = 'ahga12eg0aAbzzg'
ret15 = re.match('\w+', text2)
print(ret15.group())

# TODO: 11. ? 匹配的字符可以出现一次或者不出现（0或者1）
"""
可有可无，最多一个
"""

print(r'11. ? 匹配的字符可以出现一次或者不出现（0或者1）')
text3 = 'abcd'
ret16 = re.match('\w?', text3)
print(ret16.group())

# TODO: 12. 匹配m-n个字符。在这中间的字符都可以匹配到
"""
{m}: 匹配m个字符
{m,}: 匹配最少m个字符至所有
{m,n}: 匹配m-n个字符
{,n}:匹配最少0个，最多n个字符
"""
print('12. 匹配m-n个字符。在这中间的字符都可以匹配到...')
# text4 = '400 811 9092'
# ret17 = re.match('[\d+\s*]+', text4)

text4 = 'a4a008119092avgasg'
ret17 = re.match('\d{,5}', text4)
print(ret17.group())
