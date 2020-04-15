# 题目<1>
name = input("请输入姓名：")
sex = input("请输入性别：")
age = input("请输入年龄：")
personalInform = {"姓名": name, "性别": sex, "年龄": age}
# personalInform = {"姓名": input("请输入姓名："), "性别": input("请输入性别："), "年龄": input("请输入年龄：")}

# 题目<2>
print("我的名字{0},今年{1}岁,性别{2},喜欢敲代码".format(personalInform["姓名"], personalInform["年龄"], personalInform["性别"]))

# 题目<3>
personalInform["身高"] = input("请输入身高：")
personalInform["联系方式"] = input("请输入联系方式：")

# 题目<4>
for key, val in personalInform.items():
    print(key + ":", val)

# 题目<5>
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li = list({}.fromkeys(li).keys())  # 使用字典的方法，不会改变顺序
print(li)
print("元素的数量：", len(li))

# 题目<6>
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("切片结果：", li[2::3])
'''
 第一个数字表示切片开始位置（默认为0）。
 第二个数字表示切片截止（但不包含）位置（默认为列表长度）。
 第三个数字表示切片的步长（默认为1），当步长省略时可以顺便 省略后一个冒号。
 '''

# 题目<7>
s = 'python java php'
print("切片结果：", "\'"+s[7:11]+"\'")
