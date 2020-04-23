# coding=utf-8
import re

print '第一题'
best_language = "PHP is the best programming language in the world! "
if 'PHP' in best_language:
    best_language = best_language.replace('PHP', 'Python')
print best_language

print '第二题'
Number = input('请输入1-7中的某个数字：')
Number = int(Number)
week = ['一', '二', '三', '四', '五', '六', '日']
print '今天是周' + week[Number - 1]

print '第三题'
best_language = "PHP is the best programming language in the world! "
result = re.search('[a-z]+$', best_language)
if result:
    print '全部小写'
else:
    print '不是全部小写'

print '第四题'
String = raw_input('输入字符串:')
result = re.findall(r'\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}', String)
for i in range(len(result)):
    print result[i]

print '第五题'
Text = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
result = []
for string in Text:
    result.append(re.findall(r'(\d{4}).(\d{1,2}).(\d{1,2})', string))
for oneResult in result:
    for item in oneResult:
        print item[0]+'-'+item[1]+'-'+item[2]