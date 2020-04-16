#题目<1>
name=input("请输入姓名:")
gender=input("请输入性别:")
age=input("请输入年龄:")
dict={'姓名':name,'性别':gender,'年龄':age}
print(dict)
#题目<2>
print('我的名字'+dict['姓名'],',今年'+dict['年龄'],'岁，性别'+dict['性别'],',喜欢敲代码')
#题目<3>
height=input("请输入身高：")
contact=input("请输入联系方式：")
dict['身高']=height
dict['联系方式']=contact
print(dict)
#题目<4>
for keys,values in dict.items():
    print(keys,values)
#题目<5>
li = [11,22,33,22,22,44,55,77,88,99,11]
sli=set(li)
print(len(sli))
#题目<6>
li = [1,2,3,4,5,6,7,8,9]
print(li[2::3])
#题目<7>
s = 'python java php'
print(s[7:11])
                print('公鸡是%s只，母鸡是%s只，小鸡是%s只'%(x,y,z))