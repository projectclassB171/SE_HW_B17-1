# 题目<1>
name = str(input('请输入姓名：'))
sex = str(input('请输入性别：'))
age = str(input('请输入年龄：'))
dict = {
    '''姓名''': name,
    '''性别''': sex,
    '''年龄''': age
}
# print(dict)

# 题目<2>
print('我的名字是 '+name+"，", end="")
print('今年'+age+"岁，", end="")
print('性别 '+sex+"，", end="")
print('喜欢敲代码')

# 题目<3>
dict["身高"] = str(input('身高：'))
dict["联系方式"] = str(input('联系方式：'))
# print(dict)

# 题目<4>
for key, value in dict.items():
    print(key+":", value)

# 题目<5>
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99]
s = set(li)
li = list(s)
print(len(li))

# 题目<6>
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = li[2:9:3]
print(x)

# 题目<7>
s = 'python java php'
print(s[7:11])