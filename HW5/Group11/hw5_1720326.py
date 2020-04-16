#coding=utf-8
#1.某比赛需要获取你的个人信息，设计一个程序，运行时分别提醒用户输入 姓名、性别、年龄 ，输入完了，请将数据存储为一个字典。
name = input("请输入姓名：")
gender = input("请输入性别：")
age = input("请输入年龄：")
dic = {}
dic.update({"name": name, "gender": gender, "age": age})
print(dic)

#2.数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码。
print("我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dic["name"], dic["gender"], dic["age"]))

#3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 要求提醒用户输入身高、联系方式，把数据添加到1中创建的字典。
high = input("请输入您的身高：")
mobil_phone = input("请输入您的联系方式：")
dic.update({"high": high, "mobil_phone": mobil_phone})
print(dic)

#4.用循环输出任务3完成后的字典中的所有信息。
for key, value in dic.items():
    print(key, ':', value)

#5.当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量。
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
s = set(li)
li = list(s)
print(li)
print(len(li))

#6.li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]。
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])

#7.s = 'python java php',通过切片获取: ‘java’。
s = 'python java php'
print(s[7:11])





