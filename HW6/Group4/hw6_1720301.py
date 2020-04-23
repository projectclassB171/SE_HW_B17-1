'''
1.将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world! "
'''
import re
best_language = "\n<1> PHP is the best programming language in the world! "
print(best_language.replace("PHP", "Python"))


'''
2.编写代码，提示用户输入1 - 7七个数字，分别代表周一到周日，打印输出“今天是周几”
'''
num =int(input('\n<2> 请输入1-7之间的数字：'))
week = ['周一','周二','周三','周四','周五','周末','周末']
str = '今天是{}'.format(week[num-1])
print(str)


'''
3.给定一个字符串： Python is the BEST programming Language！
编写一个正则表达式用来判断该字符串是否全部为小写。
'''
import re
string="Python is the BEST programming Language！"
k=re.search('^[a-z]+$/',string)
if k:
    print("\n<3> 全部为小写")
else:
    print("\n<3> 不是全部为小写")


'''
4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，
电话号码的格式假定为：（xxx） xxx - xxxx或xxx - xxx - xxxx。
'''
import re
str4 = '她留下了电话号码(086)258-8639，我在犹豫该不该打给打她'
result=re.findall(r"\(\d{3}.{1,2}\d{3}-\d{4}|\d{3}.{1,2}\d{3}-\d{4}",str4)
print("\n<4> 电话号码为：",result[0])


'''
5.利用正则表达式从下列不同的字符串中获取指定格式的日期。
日期的格式为yyyy - mm - dd。
'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
'''
import re
string ='今天是2022/9/24, 今天是2017/09/25, 今天是2012-07-25, 今天是2020年04月25'
result=re.findall(r'\d{4}-\d?\d-\d?\d',string)
print("\n<5> ",result[0])