"""
2020/01/05 22:42
170.【json文件处理】load成Python对象
"""
import json


# TODO: 将一个json字符串load成Python对象
json_str = '[{"name": "知了", "age": 20, "country": "china"}, {"name": "课堂", "age": 21, "country": "china"}]'
persons = json.loads(json_str, encoding='utf-8')
print('将一个json字符串load成Python对象......')
print(persons)


# TODO: 直接从文件中读取json
print('直接从文件中读取json.....')
with open('./persons.json', 'r', encoding='utf-8') as fp:
    persons_list = json.load(fp)
    for person in persons_list:
        print(person)