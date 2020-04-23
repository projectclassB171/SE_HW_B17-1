#1 将给定字符串的PHP替换为Python best_language ="PHP is the best programming language in the world! "
string=" best_language=PHP is the best programming language in the world! "
list_1=["PHP"]
for words in list_1:
    if words in string:
        print(string.replace(words,"Python"))


#2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
s = input("请输入1-7数字：")
print("今天是周{}".format(s))


#3 给定一个字符串： Python is the BEST programming Language！编写一个正则表达式用来判断该字符串是否全部为小写。
import re
s1='Python is the BEST programming Language！'
a = re.search('^[a-z]+$', s1)
if a:
  print ("s1:",a.group(), "全为小写")
else:
  print (s1, "不全是小写！")


#4  读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：（xxx） xxx-xxxx或xxx-xxx-xxxx。
import re
s1='她的电话号码是(123)222-3333'
s2= re.findall(r"\(\d{3}.{1,2}\d{3}-\d{4}|\d{3}.{1,2}\d{3}-\d{4}",s1)
print("电话号码为：",s2[0])


#5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
import re
s1 = '今天是2022/9/24, 今天是2017/09/25, 今天是2012-07-25, 今天是2020年04月25'
s2 = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", s1)
print("".join(s2))


