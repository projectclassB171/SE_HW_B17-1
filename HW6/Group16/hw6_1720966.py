#1
#将给定字符串的PHP替换为Python
#best_language = "PHP is the best programming language in the world! "
best_language = "PHP is the best programming language in the world! "
best_language1 = best_language.replace("PHP","Python")
print(best_language1)

#2
#编写代码，提示用户输入1 - 7
#七个数字，分别代表周一到周日，打印输出“今天是周几”
weekday = ("一", "二", "三", "四", "五", "六", "日")
date = int(input('请输入数字1-7:'))
print("今天是周{}".format(weekday[date - 1]))

#3
#给定一个字符串： Python is the BEST programming Language！
#编写一个正则表达式用来判断该字符串是否全部为小写。
import re
text = 'Python is the BEST programming Language！'
if re.search('[A-Z]', text):
    print("不全为小写")
else:
    print("全为小写")

#4
#读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#（xxx） xxx - xxxx或xxx - xxx - xxxx。
import re
text = '我的电话是180-767-8888还有一个电话是(210)888-1111'
a = re.findall(r'(\d{3})-(\d{3})-(\d{4})|\((\d{3})\)(\d{3})-(\d{4})', text)
print(a)

#5
#利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy - mm - dd。
#'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25'
import re
date1 = "今天是2022/9/24, 今天是2017/09/25, 今天是2012-07-25, 今天是2020年04月25"
d = re.findall(r'(\d{4}).(\d{1,2}).(\d{1,2})', date1)
print(d)
for item in d:
    print(item[0], item[1], item[2], sep='-')