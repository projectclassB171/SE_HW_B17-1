﻿1. 某比赛需要获取你的个人信息，设计一个程序，
运行时分别提醒用户输入 姓名、性别、年龄 ，输入完了，请将数据存储为一个字典，
print('-------比赛信息录入---------')
name=input('请输入你的名字：')
sex=input('请输入你的性别：')
age=input('请输入你的年龄：')
info_dict = {}
字典新增数据
info_dict['姓名'] = name
info_dict['性别'] = sex
info_dict['年龄'] = age
print(info_dict)  输出字典内容
print('-------录入完成---------')

2、数据存储完了，然后输出个人介绍，格式如下:
我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
print(f"我的名字{info_dict['姓名']}，今年{info_dict['年龄']}岁，性别{info_dict['性别']}，喜欢敲代码")

3. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 要求提醒用户输入身高、联系方式，把数据添加到1中创建的字典。
height=input('请输入您的身高：')
tel=input('请输入您的联系方式：')
info_dict['身高']=height
info_dict['联系方式']=tel

4 用循环输出任务3完成后的字典中的所有信息，格式如下（5项数据之间没有顺序要求）：
print('-------打印字典所有信息-------')
for key,values in info_dict.items():
    姓名 ： xxx
    性别： xxx
    年龄： xx
    身高： xx
    联系方式：xx
    print(f'{key}:{values}')

5. 当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量
li = [11,22,33,22,22,44,55,77,88,99,11]
li=set(li)
print(li)  {33, 99, 11, 44, 77, 22, 55, 88}
li=list(li)
print(li)        [33, 99, 11, 44, 77, 22, 55, 88]
print(len(li))   8

6.li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
li=[1,2,3,4,5,6,7,8,9]
print(li[2::3])   [3, 6, 9]

7.s = 'python java php',通过切片获取: ‘java’
s = 'python java php'
print(s[7:11])    java
