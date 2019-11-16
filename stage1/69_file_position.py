"""
2019/11/16 13:33
69.【Python文件】文件定位之tell方法
"""

# TODO: 1.tell()函数：获取当前文件指针的位置，即光标位置

fp1 = open('./test.txt', 'r', encoding='utf-8')
start_position = fp1.tell()
print('start_position: {}'.format(start_position))
text = fp1.read()
print(text)
end_position = fp1.tell()
print('end_position: {}'.format(end_position))
fp1.close()
print('=' * 50)

"""
2019/11/16 13:58
70.【Python文件】文件定位之seek方法
"""

# TODO: 2.seek(offset, from)方法：定位到某个位置，如果在读写文件的过程中，需要从另外一个位置进行操作
"""
offset: 偏移量
from: 相对位置
    0: 表示从文件开头
    1: 表示从当前位置
    2: 表示从文件末尾

注意事项：在Python3中，如果from的值不等于0，那么offset就必须为0.
异常信息：io.UnsupportedOperation: can't do nonzero cur-relative seeks
"""

fp2 = open('./seek.txt', 'r', encoding='utf-8')
# TODO: 从文件开头，向后偏移6个字符读取文件
# fp2.seek(6, 0)
# txt = fp2.read()
# print(txt)

# TODO: 从当前位置，向后偏移6个字符读取文件
# fp2.seek(6, 1)
# txt = fp2.read()
# print(txt)

# TODO: 从文件末尾10个字节处，读取文件
# TODO: io.UnsupportedOperation: can't do nonzero end-relative seeks
# fp2.seek(-10, 2)

# TODO: 先把文件指针移动到文件末尾
fp2.seek(0, 2)
end = fp2.tell()  # TODO: 57
print(end)
read_position = end - 10  # TODO: 47
print(read_position)

# TODO: 从文件开头，向后偏移read_position个字符读取文件
fp2.seek(read_position, 0)
print(fp2.tell())   # TODO: 47
txt = fp2.read()
print(txt)

fp2.close()
