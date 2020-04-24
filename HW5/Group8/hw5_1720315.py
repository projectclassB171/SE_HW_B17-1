#（1）某比赛需要获取你的个人信息，设计一个程序，运行时分别提醒用户输入 姓名、性别、年龄 ，输入完了，请将数据存储为一个字典

name = input("请输入你的姓名:")

sex = input("请输入你的性别:")

age = input("请输入你的年龄：")

dic = {}               #直接使用 {} 建立空字典

dic["name"] = name

dic["sex"] = sex

dic["age"] = age

print(dic)

#（2）数据存储完了，然后输出个人介绍，格式如下: 我的名字易星作，今年20岁，性别男，喜欢敲代码

name = input("请输入你的姓名:")

sex = input("请输入你的性别:")

age = int(input("请输入你的年龄:"))

dic = {'name': '易星作', 'sex': '男','age':'20'}

dic["name"] = name

dic["sex"] = sex

dic["age"] = age

print("我的名字%s,今年:%d，性别:%s,喜欢敲代码"%(dic["name"],dic["age"],dic["sex"]))

#（3）有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 要求提醒用户输入身高、联系方式，把数据添加到1中创建的字典。

height = input("请输入你的身高：")

telephone = input("请输入你的联系方式：")

dic = {'name': '易星作', 'sex': '男','age':'20'}

dic["height"] = height

dic["telephone"] = telephone

print(dic)

#(4)用循环输出任务3完成后的字典中的所有信息

for key in dic:

    print(key+':'+str(dic.get(key)))

#(5)当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，请去除重复元素之后，再统计元素的数量

li = [11,22,33,22,22,44,55,77,88,99,11]

set = set(li)

li = list(set)

print(len(li))

#（6）li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]

number = [1,2,3,4,5,6,7,8,9,10]

num_str_1 = number[2::3]

print(num_str_1)

#(7)s = 'python java php',通过切片获取: ‘java’

s ='python java php'

num_str_1 = s[7:11]

print(num_str_1)