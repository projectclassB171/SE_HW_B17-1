# coding=gbk
#题目<1>
name = input("请输入你的姓名:")
gender = input("请输入你的性别:")
age = input("P请输入你的年龄:")
dic = {}
dic.update({"姓名": name, "性别": gender, "年龄": age})

#题目<2>
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dic["姓名"], dic["年龄"], dic["性别"]))

#题目<3>
high = input("请输入您的身高：")
mobil_phone = input("请输入您的联系方式：")
dic.update({"身高": high, "联系方式": mobil_phone})

#题目<4>
for k, v in dic.items():
    print(k + ':' + v)

#题目<5>
li = [11,22,33,22,22,44,55,77,88,99,11]
s = set(li)
li = list(s)
print(len(li))

#题目<6>
li = [1,2,3,4,5,6,7,8,9]
print(li[2::3])

#题目<7>
s = 'python java php'
print(s[7: 11])

