# 题目<1>
best_language = "PHP is the best programming language in the world!"
keyWord = "PHP"
print(best_language.replace(keyWord, "Python"))

# 题目<2>
weeks = "一二三四五六日"
num = eval(input("请输入1-7内的数字："))
if num in range(1, 8):
    print("周{}".format(weeks[num - 1]))

# 题目<3>
import re

line = "Python is the BEST programming Language!"
res = r'^[a-z\s]*$'
if re.match(res, line):
    print("全是小写")
else:
    print("不全是小写")

# 题目<4>
import re
lines = input("请输入带号码的字符串：")
phone = re.findall(r'\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}', lines)
print("".join(phone))

# 题目<5>
import re
text = '今天是2022/9/24, 今天是2017/09/25, 今天是2012-07-25, 今天是2020年04月25'
result = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", text)
print("".join(result))
