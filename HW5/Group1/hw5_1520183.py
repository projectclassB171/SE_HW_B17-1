# 题目<1>
name = input("输入姓名：")
sex = input("输入性别：")
age = input("输入年龄：")
dic = {}
dic.update({"姓名": name, "性别": sex, "年龄": age})
print(dic)

# 题目<2>
print(f"我的名字{info_dict['姓名']}，今年{info_dict['年龄']}岁，性别{info_dict['性别']}，喜欢敲代码")

# 题目<3>
personalInform["身高"] = input("请输入身高：")
personalInform["联系方式"] = input("请输入联系方式：")

# 题目<4>
for i in dic:
    print("{}:{}".format(i,dic[i]))

# 题目<5>
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set(li)
li = list(s)
print(li)
print(len(li))

# 题目<6>
li=[1,2,3,4,5,6,7,8,9]
print(li[2::3])

# 题目<7>
s = 'python java php'
print("切片结果：", "\'"+s[7:11]+"\'")
