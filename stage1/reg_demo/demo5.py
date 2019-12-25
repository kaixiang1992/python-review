"""
2019/12/25 23:21
163.【正则表达式】group分组
"""
import re

"""
分组: 
在正则表达式中，可以对过滤到的字符串进行分组。分组使用圆括号的方式。
1.group()和group(0)是等价的，返回的是整个满足条件的字符串。
2.groups()返回的是里面的子组(元祖)。索引从1开始。
3.group(1)：返回的是第一个子组，可以传入多个group(1, 2)返回元祖。
"""

print('%sgroup分组%s' % ('-' * 20, '-' * 20))
sale_price = 'apple price is $99,orange price is $10'
sale_ret = re.search('.*(\$\d+).*(\$\d+).*', sale_price)
print('group(): ', sale_ret.group())
print('group(0): ', sale_ret.group(0))
print('group(1): ', sale_ret.group(1))
print('group(2): ', sale_ret.group(2))
print('group(1, 2): ', sale_ret.group(1, 2))
print('groups(): ', sale_ret.groups())  # TODO: 索引从1开始

"""
2019/12/25 23:36
165.【正则表达式】re模块常用函数
"""

"""
findall:
找出所有满足条件的，返回的是一个列表
"""

print('%s常用函数findall%s' % ('-' * 20, '-' * 20))
find_allprice = 'apple price is $99,orange price is $10'
find_allret = re.findall('\$\d+', find_allprice)
print(find_allret)

"""
sub:
用来替换字符串。将匹配到的字符串替换为其他字符串。
"""

print('%s常用函数sub%s' % ('-' * 20, '-' * 20))
sub_text = 'apple price is $99,orange price is $10'
sub_text = re.sub('\$\d+', '0', sub_text)
print(sub_text)

print('%s常用函数sub案例处理html标签信息%s' % ('-' * 20, '-' * 20))
html = """
<dd class="job_bt">
<h3 class="description">职位描述：</h3>
<div class="job-detail">
<p>1.以Python开发为主，建议必须具备python开发能力；</p>
<p>2.至少两年以上开发经验或者测开经验，只有测试经验不可以；</p>
<p>3.对于linux的管理、维护、使用要熟悉，基础命令要能回答上来；</p>
<p>4.对于常用数据库（例如mysql）要熟练使用，至少常用的增删改查要会；</p>
<p>5.对于第5条加分项仅做确认了解；</p>
<p>6.需要计算机专业毕业</p>
</div>
</dd>
"""

ret_html = re.sub('<.+?>', '', html)
print(ret_html)

"""
split:
使用正则表达式来分割字符串。
"""

print('%s常用函数split%s' % ('-' * 20, '-' * 20))
txt = 'hello&world ni hao'
txt_ret = re.split('\s|&', txt)
print(txt_ret)

"""
compile:
对于一些经常要用到的正则表达式，可以使用compile进行编译，后期再使用的时候
可以直接拿过来用，执行效率会更快。而且compile还可以指定flag=re.VERBOSE，
在写正则表达式的时候可以做好注释。
"""
print('%s常用函数compile%s' % ('-' * 20, '-' * 20))
text = 'the number is 20.50'
# r = re.compile('\d+(\.\d+)?')
r = re.compile("""
    \d+ # TODO: 至少一位到多位数字
    (\.\d+)? #TODO: 匹配可有可无最多一次的小数点及后面数字
""", re.VERBOSE)
text_ret = re.search(r, text)
print(text_ret.group())
