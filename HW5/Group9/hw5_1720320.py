# 题目<1>
name = input("输入姓名：")
sex = input("输入性别：")
age = input("输入年龄：")
dic = {}
dic.update({"姓名": name, "性别": sex, "年龄": age})
print(dic)

# 题目<2>
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dic["name"], dic["sex"], dic["age"]))

# 题目<3>
high = input("输入您的身高：")
mobil_phone = input("输入您的联系方式：")
dic.update({"high": high, "mobil_phone": mobil_phone})
print(dic)

# 题目<4>
for i in dict:
    print("{}:{}".format(i,dict[i]))

# 题目<5>
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set(li)
li = list(s)
print(li)
print(len(li))

# 题目<6>
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("结果：", li[2::3])

# 题目<7>
s = 'python java php'
print("结果：", "\'"+s[7:11]+"\'")
