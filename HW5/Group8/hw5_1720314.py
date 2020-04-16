#1
name=input('姓名:')
age=input('年龄:')
gender=input('性别:')
msg={'姓名':name,'年龄':age,'性别':gender}
#2
print('我的名字'+msg['姓名'],',今年',msg['年龄'],'岁，性别'+msg['性别'],'，喜欢敲代码')
#3
height=input('身高：')
phone=input('联系方式：')
msg['身高']=height
msg['联系方式']=phone
#4
for k,v in msg.items():
    print(k+':'+v)
#5
li = [11,22,33,22,22,44,55,77,88,99,11]
sli=set(li)
print(len(sli))
#6
li = [1,2,3,4,5,6,7,8,9]
print(li[2::3])
#7
s = 'python java php'
print(s[7:12])