import re
#1. 将给定字符串的PHP替换为Python       
best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

#2.编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
num =int(input('请输入1-7之间的数字：'))
list1 = ['周一','周二','周三','周四','周五','周末','周末']
str1 = '今天是{}'.format(list1[num-1])
print(str1)

#3. 给定一个字符串： Python is the BEST programming Language！
string="Python is the BEST programming Language！"
k=re.search('^[a-z]+$/',string)
if k:
    print("全为小写")
else:
    print("不全为小写")

#4.读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
#  （xxx） xxx-xxxx或xxx-xxx-xxxx。
str = input("请输入字符串")
result=re.findall(r'([(]\d{3}[)]|\d{3})-?(\d{3})-(\d{4})', str)
for each in result:
    print(each[0],each[1],each[2],sep="-")


#5.利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
#  '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
datetext = '今天是2022/9/24, 今天是2017/09/25, 今天是2012-07-25, 今天是2020年04月25'
result = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", datetext)
print("".join(result))



