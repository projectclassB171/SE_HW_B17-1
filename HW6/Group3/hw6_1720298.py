''''''
import re
'''
1 将给定字符串的PHP替换为Python      
'''
best_language = "PHP is the best programming language in the world! "
change = re.sub('PHP','Python',best_language)
print("1.",change)
print()

'''
2 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
'''
date = int(input('请输入1-7中的一个数字'))
text = '零一二三四五六七'
date1 = re.sub(str(date),text[date],str(date))
print("2.今天是周{}".format(date1))
print()
'''
3 给定一个字符串： Python is the BEST programming Language！
编写一个正则表达式用来判断该字符串是否全部为小写。
'''
lines = 'Python is the BEST programming Language！'
lines = lines.strip('！')
if re.match(r'^[a-z\s]*$',lines):
    print("3.是否为全部小写: True")
else:
    print("3.是否为全部小写: False")
print()
'''
4 读取一个字符串，要求使用正则表达式来读取其中的电话号码，电话号码的格式假定为：
（xxx） xxx-xxxx或xxx-xxx-xxxx。
'''
s = '小明的手机是（135） 353-3535'
s1 = '小明的手机不是135-353-3535'
res = re.findall(r"\d{3}.{1,2}\d{3}-\d{4}",s1) #可改为s

print("4."+"".join(res))
print()
'''
5 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
'''
print("5.")
date2 = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
for i in date2:
    res = re.findall(r"\d{4}.*\d{1,2}.*\d{1,2}",i)
    res = re.sub(r'\D','-',str(res[0]))
    print("".join(res))
