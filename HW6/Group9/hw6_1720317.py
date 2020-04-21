# coding=utf-8

"""
题目一
1 将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world! "
"""
print('第一题：')
best_language = "PHP is the best programming language in the world! "
wordNeedChanged = 'PHP'
if wordNeedChanged in best_language:
    best_language = best_language.replace(wordNeedChanged, 'Python')  # string.replace()替换
print(best_language)

"""
题目二
2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
"""
print('\n第二题：')
inputNumber = int(input('请输入1-7中的某个数字：'))  # input输入了字符串，需要转换成int
week = ['一', '二', '三', '四', '五', '六', '日']
print('今天是周{}'.format(week[inputNumber - 1]))

"""
题目三
3 给定一个字符串： Python is the BEST programming Language！
编写一个正则表达式用来判断该字符串是否全部为小写。
"""
import re

print('\n第三题：')
best_language = "PHP is the best programming language in the world! "
rule = '[a-z]+$'  # [a-z]:a-z中的一个，+：匹配位于+之前的字符或子模式的1次或多次出现 ，$: 匹配行尾，匹配以$之前的字符结束的字符串
result = re.search(rule, best_language)  # re.search:在整个字符串中寻找模式，返回match对象或None
if result:
    print('全部小写')
else:
    print('不是全部小写')

"""
题目四
4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
（xxx） xxx-xxxx或xxx-xxx-xxxx。
"""
import re

print('\n第四题：')
inputString = input('请输入一串字符串: ')
rule1 = r'\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}'  # ():将位于()内的内容作为一个整体来对待,\表示位于\之后的为转义字符 ,{3}：3位
result = re.findall(rule1, inputString)  # 返回包含字符串中所有与给定模式匹配的项的列表
for i in range(len(result)):
    print(result[i])

"""
题目五
5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
"""
import re

print('\n第五题：')
dateText = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
result = []
rule1 = r'(\d{4}).(\d{1,2}).(\d{1,2})'  # 匹配除换行符以外的任意单个字符 ，{1，2}：匹配1到2位,\d匹配任何数字，相当于[0-9]，r:这个string是个raw string
for string in dateText:
    result.append(re.findall(rule1, string))
for oneResult in result:
    for item in oneResult:
        print(item[0], item[1], item[2], sep='-')  # sep函数是设置分隔符
