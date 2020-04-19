'''
题目<1>.
将给定字符串的PHP替换为Python      
best_language = "PHP is the best programming language in the world! "
'''
best_language = "PHP is the best programming language in the world! "
best_language = best_language.replace('PHP','Python')
print("题目<1>替换后的结果为:",best_language)

#题目<1>.也可采用正则表达式实现，代码如下：
#import re
#best_language = "PHP is the best programming language in the world! "
#res = re.sub('PHP','Python',best_language)
#print("".join(res))


'''
题目<2>.
编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
'''
num =int(input('题目<2>请您输入1-7之间的数字：'))
li2 = ['周一','周二','周三','周四','周五','周六','周日']
s2 = '今天是{}'.format(li2[num-1])
print("题目<2>输出结果为:",s2)


'''
题目<3>.
给定一个字符串： Python is the BEST programming Language！
编写一个正则表达式用来判断该字符串是否全部为小写。
'''
import re
s3 = 'Python is the BEST programming Language！'
res3 = re.match('[a-z]+$', s3)
if res3:
    print("题目<3>所给字符串全部为小写")
else:
    print("题目<3>所给字符串不是全部为小写")


'''
题目<4>.
读取一个字符串，要求使用正则表达式来读取其中的电话号码，
电话号码的格式假定为：（xxx） xxx-xxxx或xxx-xxx-xxxx。

'''
import re
s4 = "s(123) 456-7890heqq987-654-3210+_(987) 654-3210我的"
res4 = re.findall(r"\(\d{3}.{1,2}\d{3}-\d{4}|\d{3}.{1,2}\d{3}-\d{4}",s4)
print("题目<4>我使用的字符串为:",s4)
print("题目<4>输出电话号码为:"+",".join(res4))



'''
题目<5>.
利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
'今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
'''
import re
li5 = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
for i5 in li5:
    res5 = re.findall(r"\d{4}.*\d{1,2}.*\d{1,2}",i5)
    res5 = re.sub(r'\D','-',str(res5[0]))
    print("题目<5>以yyyy-mm-dd格式输出日期为:"+"".join(res5))







