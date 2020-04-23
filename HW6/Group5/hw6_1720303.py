#题目一1 将给定字符串的PHP替换为Python
#best_language = "PHP is the best programming language in the world! "

best_language = "PHP is the best programming language in the world! "
t1 = 'PHP'
if t1 in best_language:
    best_language = best_language.replace(t1, 'Python')
print(best_language)


#题目二 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”

t2 = int(input('请输入1-7中的某个数字：'))
week = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
print('今天是周{}'.format(week[t2 -1]))


#题目三 给定一个字符串： Python is the BEST programming Language！编写一个正则表达式用来判断该字符串是否全部为小写。

import re
t3 = 'Python is the BEST programming Language！'
t3 = t3.strip('！')
if re.match(r'^[a-z\s]*$',t3):
    print("是全部小写")
else:
    print("不是全部小写")


#题目四读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx-xxxx或xxx-xxx-xxxx。

import re
t4 = "s767-456-7890heqq987-9090-6543shwwu+_(987) 654-3210我的"
tm4 = re.findall(r"\(\d{3}.{1,2}\d{3}-\d{4}|\d{3}.{1,2}\d{3}-\d{4}",t4)
print("题目<4>我使用的字符串为:",t4)
print("题目<4>输出电话号码为:"+",".join(tm4))

#题目五 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
#'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',

import re
tg5 = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
rt5 = []
r5 = r'(\d{4}).(\d{1,2}).(\d{1,2})'
for string in tg5:
    rt5.append(re.findall(r5, string))
for oneResult in rt5:
    for item in oneResult:
        print(item[0], item[1], item[2], sep='-')
