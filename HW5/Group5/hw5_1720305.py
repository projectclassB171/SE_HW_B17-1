#题目1
name = input("请输入你的姓名:")
gender = input("请输入你的性别:")
age = input("P请输入你的年龄:")
dict={'姓名':name,'性别':gender,'年龄':age}

#题目2
print('我的名字'+dict['姓名']+',今年'+dict['年龄']+'岁，性别'+dict['性别']+',喜欢敲代码')

#题目3
height = input("请输入你的身高:")
phone = input("请输入你的联系方式:")
dict['身高']=height
dict['联系方式']=phone

#题目4
for key in dict:
    print(key+':'+dict[key])
    
#题目5
li = [11,22,33,22,22,44,55,77,88,99,11]
li = list(set(li))
print(len(li))

#题目6
li = [1,2,3,4,5,6,7,8,9]
li = li[2::3]
print(li)

#题目7
s = 'python java php'
print(s[7:11:])