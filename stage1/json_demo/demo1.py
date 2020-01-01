"""
2020/01/01 20:08
169.【json文件处理】dump成json字符串以及编码问题
"""

"""
JSON支持的数据格式：
1.对象（字典）。使用花括号。
2.数组（列表）。使用方括号。
3.整形、浮点型、布尔类型还有null类型。
4.字符串类型（字符串必须要用双引号，不能用单引号）。

多个数据之间使用逗号分开。
注意：json本质上就是一个字符串。
"""

import json

persons = [
    {
        'name': '知了',
        'age': 20,
        'country': 'china'
    },
    {
        'name': '课堂',
        'age': 21,
        'country': 'china'
    }
]

# persons_str = json.dumps(persons, ensure_ascii=False)
# print(type(persons_str))  # TODO: str
# print(persons_str)
#
# with open('./persons.json', 'w', encoding='utf8') as fp:
#     fp.write(persons_str)


with open('./persons.json', 'w', encoding='utf-8') as fp:
    json.dump(persons, fp, ensure_ascii=False)