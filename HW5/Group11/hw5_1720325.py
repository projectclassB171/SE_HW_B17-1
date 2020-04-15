# 题目1
name = input("请输入你的姓名:")
gender = input("请输入你的性别:")
age = input("P请输入你的年龄:")
dic = {}
dic.update({"姓名": name, "性别": gender, "年龄": age})

# 题目2
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dic["姓名"], dic["年龄"], dic["性别"]))

#题目3
personalInform["身高"] = input("请输入身高：")
personalInform["联系方式"] = input("请输入联系方式：")

#题目4
for key, val in personalInform.items():
    print(key + ":", val)

# 题目5
li = [11,22,33,22,22,44,55,77,88,99,11]
s = set(li)
li = list(s)
print(len(li))

# 题目6
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])

# 题目7
s = 'python java php'
print(s[7: 11])