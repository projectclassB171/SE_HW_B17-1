#题目1
name=input("请输入您的姓名：")
sex=input("请输入您的性别：")
age=input("请输入您的年龄：")
dict={
    '姓名':name,
    '性别':age,
    '年龄':sex
      }
print(dict)
#题目2
print("我的名字是",name,",""今年",age,"岁,","性别",sex,",喜欢敲代码。")

#题目3
dict["身高"]=input("身高：")
dict["联系方式"]=input("联系方式：")
print(dict)
#题目4
for keys,values in dict.items():
    print(keys,values)
#题目5
li = [11,22,33,22,22,44,55,77,88,99,11]
sli=set(li)
print(len(sli))
#题目6
li =[1,2,3,4,5,6,7,8,9]
li[2::3]
#题目7
s='python java php'
s[7:11]
