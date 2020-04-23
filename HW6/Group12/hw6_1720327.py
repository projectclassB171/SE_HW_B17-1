# 题目1
import re

best_language = "PHP is the best programming language in the world!"
print(best_language.replace("PHP","Python"))

# 题目2

num = int(input('请输入1-7之间的数字：'))
day = ['一','二','三','四','五','六','4日']
if num in range(1, 8):
    print("今天是周{}".format(day[num - 1]))

# 题目3

line3 = "Python is the BEST programming Language!"
if re.match('[a-z]+$',line3):
    print("给出的字符串全为小写")
else:
    print("给出的字符串不全为小写")

# 题目4

line4 = "xxx的电话号码是123-456-7890或(123) 456-7890"
phonenum = re.findall(r"\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}",line4)
print("电话号码为:"+"".join(phonenum))

# 题目5

line5 = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
for date in line5:
    datetime = re.findall(r"\d{4}.*\d{1,2}.*\d{1,2}",date)
    datetime = re.sub(r'\D','-',str(datetime[0]))
    print("其中的日期有:"+"".join(datetime))