"""
2020/01/05 22:58
172.【csv文件处理】写入csv文件的两种方式
"""
import csv

# TODO: 写入数据到csv文件
'''
写入数据到csv文件，需要创建一个writer对象，主要用到两个方法。
一个是writerow，这个是写入一行。
一个是writerows，这个是写入多行。
'''


def write_csv_demo1():
    headers = ['name', 'age', 'country']
    values = [
        ('知了', 20, 'china'),
        ('课堂', 21, 'china')
    ]
    with open('./persons.csv', 'w', encoding='utf-8', newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)


# TODO: 可以使用字典的方式把数据写入进去。这时候就需要使用DictWriter了
def write_csv_demo2():
    headers = ['name', 'age', 'country']
    values = [{"name": "知了", "age": 20, "country": "china"}, {"name": "课堂", "age": 21, "country": "china"}]
    with open('./persons.csv', 'w', encoding='utf-8', newline="") as fp:
        writer = csv.DictWriter(fp, headers)
        # TODO: 写入表头数据的时候，需要调用writeheader方法
        writer.writeheader()
        writer.writerows(values)
        writer.writerow({"name": "joke", "age": 22, "country": "usa"})


if __name__ == '__main__':
    write_csv_demo2()
