"""
2019/12/24 22:50
163.【正则表达式】转义字符和原生字符串
"""
import re

"""
转义字符：
在正则表达式中，有些字符是有特殊意义的字符。因此如果想要匹配这些字符，那么就必须使用反斜杠进行转义。
比如$代表的是以$结尾，如果想要匹配$，那么就必须使用\$
"""

# TODO: 1.转义字符
sale = 'iPhone price is $399'
ret_sale = re.search('\$\d+', sale)
print('转义字符....')
print(ret_sale.group())

"""
原生字符串:
在正则表达式中，\是专门用来做转义的。在Python中\也是用来做转义的。因此如果想要在
普通的字符串中匹配出\，那么要给出四个\
"""

# TODO: 2.原生字符串

raw_text = r'\n'
print('原生字符串...')
print(raw_text)

# TODO: 3.正则匹配原生字符串
text = '\\c'
"""
python中:
\\n => \n
\\\\n => \\n

正则表达式:
\\n => \n
"""

ret = re.match(r'\\c', text)
print('正则匹配原生字符串...')
print(ret.group())
