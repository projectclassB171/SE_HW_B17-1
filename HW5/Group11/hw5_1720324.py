#coding:utf-8

1.
dict = {}
name,gender,age = input("请依次输入姓名，性别，年龄，用空格分开").split()
dict['姓名'] = name
dict['性别'] = gender
dict['年龄'] = age
print("1.",dict)

'''
2.
'''
print("2.我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(dict['姓名'],dict['年龄'],dict['性别']))

'''
3.
height,phone = input("请依次输入身高、联系方式，用空格分开").split()
dict['身高'] = height
dict['联系方式'] = phone
print("3.",dict)

'''
4 
print("4.")
for i in dict:
    print("{}:{}".format(i,dict[i]))

'''
5. 
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












