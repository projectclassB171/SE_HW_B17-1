# 题目<1>
name = input("请输入姓名：")
sex = input("请输入性别：")
age = input("请输入年龄:")
dic = {'姓名': name, '性别': sex, '年龄': age}

# 题目<2>
print('我的名字', dic['姓名'], ', 今年', dic['年龄'], '岁, 性别', dic['性别'], ', 喜欢代码')

# 题目<3>
tall = input("请输入身高：")
phone = input("请输入联系方式：")
dic['身高'] = tall
dic['联系方式'] = phone

# 题目<4>
for key, value in dic.items():
    print(key, ':', value)

# 题目<5>

li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s_li = set(li)
print(len(s_li))

# 题目<6>
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])

# 题目<7>
s = 'python java php'
print(s[7:11])