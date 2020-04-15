#coding:utf-8
''''''
'''
1.某比赛需要获取你的个人信息，设计一个程序，
运行时分别提醒用户输入 姓名、性别、年龄 ，输入完了，请将数据存储为一个字典，
'''
dict = {}
name,gender,age = input("请依次输入姓名，性别，年龄，用空格分开").split()
dict['姓名'] = name
dict['性别'] = gender
dict['年龄'] = age
print("1.",dict)

'''
2.数据存储完了，然后输出个人介绍，格式如下:
我的名字XXX，今年XXX岁，性别XX，喜欢敲代
码
'''
print("2.我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dict['姓名'],dict['年龄'],dict['性别']))

'''
3.有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 要求提醒用户输入身高、联系方式，把数据添加到1中创建的字典。
'''
height,phone = input("请依次输入身高、联系方式，用空格分开").split()
dict['身高'] = height
dict['联系方式'] = phone
print("3.",dict)

'''
4 用循环输出任务3完成后的字典中的所有信息，格式如下（5项数据之间没有顺序要求）：
姓名 ： xxx
性别： xxx
年龄： xx
身高： xx
联系方式：xx
'''
print("4.")
for i in dict:
    print("{}:{}".format(i,dict[i]))

'''
5. 当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量
'''
print("5.",end=" ")
li = [11,22,33,22,22,44,55,77,88,99,11]
li2 = set(li)
li2 = list(li2)
print(li2)
print("元素数量为：{}".format(len(li2)))

'''
6.li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
'''
li = [1,2,3,4,5,6,7,8,9]
print("6.结果：{}".format(li[2::3]))

'''
7.s = 'python java php',通过切片获取: ‘java’
'''
print("7.",end=" ")
s = 'python java php'
print("‘{}’".format(s[7:11]))












