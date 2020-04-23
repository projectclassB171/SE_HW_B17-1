#(1)将给定字符串的PHP替换为Python


t='best_language = PHP is the best programming language in the world! '
t1=t.replace('PHP','python')
print(t1)

#(2)编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”


s="一二三四五六日"
c=eval(input("请输入1-7内的数字："))
if c in range(1,8):
 print("今天为星期{}".format(s[c-1]))

#(3)给定一个字符串： Python is the BEST programming Language！编写一个正则表达式用来判断该字符串是否全部为小写


import re

best_language = "PHP is the best programming language in the world! "
rule = '[a-z]+$'
result = re.search(rule, best_language)
if result:
    print('全部为小写')
else:
    print('不是全部为小写')

#（4）读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx-xxxx或xxx-xxx-xxxx。


def find(a):
 phone = re.findall(r"(\d{3})\-(\d{3})\-(\d{4})|\((\d{3})\)\s(\d{3})\-(\d{4})", a)
 print("phone: ", phone)
str2 = input("请输入一个含有电话号码的字符串:")
find(str2)

#（5）利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
#     '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',


DateText = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
result = []
rule1 = r'(\d{4}).(\d{1,2}).(\d{1,2})'
for string in DateText:
    result.append(re.findall(rule1, string))
for oneResult in result:
    for item in oneResult:
        print(item[0], item[1], item[2], sep='-')