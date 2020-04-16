#题目1

name = input("请输入你的姓名：")
sex = input("请输入你的性别：")
age = input("请输入你的年龄：")
dic = {}
dic.update({"姓名": name, "性别": sex, "年龄": age})
print(dic)

#题目2

print('我的名字'+dict['姓名'],',今年'+dict['年龄'],'岁，性别'+dict['性别'],',喜欢敲代码')

#题目3

height = input("请输入你的身高：")
phonenum = input("请输入你的联系方式：")
dict['身高'] = height
dict['联系方式'] = phonenum
print(dict)

#题目4

for i in dict:
print("{}:{}".format(i,dict[i]))

#题目5

li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set(li)
li = list(s)
print(len(li))

#题目6

li = [1,2,3,4,5,6,7,8,9]
print(li[2::3])

#题目6

s = 'python java php'
print(s[7: 11])