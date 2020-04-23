''''''
import re
#支持正则表达式
'''
1、将给定字符串的PHP替换为Python.
    best_language = "PHP is the best programming language in the world! "
'''
best_language = "PHP is the best programming language in the world! "
replaces = re.sub('PHP','Python',best_language)
print("1.",replaces)
print()

'''
2、编写代码，提示用户输入1-7七个数字，
    分别代表周一到周日，打印输出“今天是周几”
'''
date = int(input('请输入1-7中的一个数字:'))
text = '一二三四五六日'
date1 = re.sub(str(date),text[date-1],str(date))
print("2.今天是周{}".format(date1))
print()
'''
3、给定一个字符串： Python is the BEST programming Language！
    编写一个正则表达式用来判断该字符串是否全部为小写。
'''
#Python is the BEST programming Language！
strs1 = 'Python is the BEST programming Language！'
print("3.1、验证是否全为小写："+strs1+"\n")
strs1 = strs1.replace('！', '')
if re.match(r'^[a-z\s]*$',strs1):
    print("结果：[True]全为小写")
else:
    print("结果：[False]不全为小写")
print()
#python is the best programming language！
strs2 = 'python is the best programming language！'
print("3.2、验证是否全为小写："+strs2+"\n")
strs2 = 'python is the best programming language！'
strs2 = strs2.replace('！', '')
if re.match(r'^[a-z\s]*$',strs2):
    print("结果：[True]全为小写")
else:
    print("结果：[False]不全为小写")
print()
'''
4、读取一个字符串，要求使用正则表达式来读取其中的电话号码，
    电话号码的格式假定为：
    （xxx） xxx-xxxx或xxx-xxx-xxxx。
'''
tel1 = 'joan的手机是（182）272-2727'
tel2 = 'joan的手机不是182-272-2727'
#（xxx） xxx-xxxx
res1 = re.findall(r".\d{3}.{1,2}\d{3}.\d{4}",tel1)
#xxx-xxx-xxxx
res2 = re.findall(r"\d{3}-{1,2}\d{3}-\d{4}",tel2)
print("4."+" ".join(res1))
print("4."+" ".join(res2))
print()
'''
5、利用正则表达式从下列不同的字符串中获取指定格式的日期。
    日期的格式为yyyy-mm-dd。
    '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
'''
print("5.")
dates = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
for i in dates:
    res = re.findall(r"\d{4}.*\d{1,2}.*\d{1,2}",i)
    res = re.sub(r'\D','-',str(res[0]))
    print("".join(res))
