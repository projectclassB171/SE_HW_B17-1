import re
# 1.将给定字符串的PHP替换为Python
best_language = "PHP is the best programming language in the world! "
best_language= best_language.replace('PHP','Python')
print('第一题：',best_language)


#2. 编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
data_input = int(input('第二题：请输入1-7之间的数字'))
list_data = ['周一','周二','周三','周四','周五','周六','周日']
output = '今天是{}'.format(list_data[data_input-1])
print(output)


#3. 给定一个字符串： Python is the BEST programming Language！
#   编写一个正则表达式用来判断该字符串是否全部为小写。
t_3 = 'Python is the BEST programming Language！'
if re.match('[a-z]+$',t_3):
    print("第三题：字符串全为小写")
else:
    print("第三题：字符串不全为小写")


#4. 读取一个字符串，要求使用正则表达式来读取其中的电话号码，
#   电话号码的格式假定为：（xxx） xxx-xxxx或xxx-xxx-xxxx。
t_4 = '我的手机号为131-2235-2926'
res = re.findall(r"\d{3}[-\/]\d{4}[-\/]\d{4}",t_4)
print('第四题：手机号为：',res)


#5. 利用正则表达式从下列不同的字符串中获取指定格式的日期。日期的格式为yyyy-mm-dd。
#  '今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25',
t_5 = ['今天是2022/9/24', '今天是2017/09/25', '今天是2012-07-25', '今天是2020年04月25']
for i in t_5:
    res= re.findall(r"\d{4}[-]\d{2}[-]\d{2}",i)
    if res != []:
        print('第五题:',res)