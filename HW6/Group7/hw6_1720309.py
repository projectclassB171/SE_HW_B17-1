"""1.将给定字符串的PHP替换为python"""
best_language = "PHP is the best programming language in the world! "
print(best_language.replace('PHP', 'python'))


"""2.编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”。"""
week_input = input("请输入1-7数字：")
print("今天是周{}".format(week_input))


"""3.给定一个字符串，Python is the BEST programming Language!
编写一个正则表达式用来判断该字符串是否全部为小写。"""
import re
text1 = "Python is the BEST programming Language!"
an = re.search('[a-z]+$', text1)
if an:
    print('s1:', an.group(), '该字符串全部为小写!')
else:
    print('s1:', '该字符串不全是小写!')


"""4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为:
(xxx)xxx-xxxx或xxx-xxx-xxxx。"""
import re
test_tellnum1 = '1234567890,123-456-7890,(123)456-789'
mat1 = re.search(r"(\d{3}-\d{3}-\d{4})", test_tellnum1)
print(mat1.groups())


"""5.利用正则表达式从下列不同的字符串中获取指定格式的日期，日期的格式为yyyy-mm-dd。
'今天是2022/9/24','今天是2017/09/25','今天是2012-07-25','今天是2020年04月25'."""
import re
test_date1 = '今天是2022/9/24,今天是2017/09/25,今天是2012-07-25,今天是2020年04月25'
mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", test_date1)#指定日期格式为yyyy-mm-dd
print(mat.groups())
print(mat.group(0))




