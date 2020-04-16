# 题目<1>某比赛需要获取你的个人信息，设计一个程序，运行时分别提醒用户输入 姓名、性别、年龄 ，输入完了，请将数据存储为一个字典，
name = input("请输入姓名：")
sex = input("请输入性别：")
age = input("请输入年龄：")
personalInform = {"姓名": name, "性别": sex, "年龄": age}


# 题目<2> 数据存储完了，然后输出个人介绍，格式如下:
print("我的名字{0},今年{1}岁,性别{2},喜欢敲代码".format(personalInform["姓名"], personalInform["年龄"], personalInform["性别"]))

# 题目<3>有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 要求提醒用户输入身高、联系方式，把数据添加到1中创建的字典。
personalInform["身高"] = input("注意：请输入身高：")
personalInform["联系方式"] = input("注意：请输入联系方式：")

# 题目<4>用循环输出任务3完成后的字典中的所有信息
for key, val in personalInform.items():
    print(key + ":", val)

# 题目<5>当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li = list({}.fromkeys(li).keys())
print(li)
print("元素的数量：", len(li))

# 题目<6>li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("切片结果：", li[2::3])


# 题目<7>s = 'python java php',通过切片获取: ‘java’
s = 'python java php'
print("切片结果：", "\'"+s[7:11]+"\'")

