"""
2020/01/05 22:48
171.【csv文件处理】读取csv文件的两种方式
"""

import csv


# TODO: 以列表形式读取csv文件数据
def read_csv_demo1():
    with open('./stock.csv', 'r') as fp:
        render = csv.reader(fp)
        # TODO: 跳过表头读取
        next(render)
        for x in render:
            name = x[3]
            volumn = x[len(x) - 1]
            print({'name': name, 'volumn': volumn})


# TODO: 以字典形式读取csv文件数据
def read_csv_demo2():
    with open('./stock.csv', 'r') as fp:
        render = csv.DictReader(fp)
        for x in render:
            name = x['secShortName']
            volumn = x['turnoverVol']
            print({'name': name, 'volumn': volumn})



if __name__ == '__main__':
    read_csv_demo2()
