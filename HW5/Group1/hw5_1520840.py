#题目(1)
name=input('请输入姓名:')
age=input('请输入年龄:')
gender=input('请输入性别:')
msg={
    '姓名':name,
    '年龄':age,
    '性别':gender
}
#题目(2)
print('我的名字'+msg['姓名'],',今年',msg['年龄'],'岁，性别'+msg['性别'],'，喜欢敲代码')
#题目(3)
height=input('请输入身高：')
phone=input('请输入联系方式：')
msg['身高']=height
msg['联系方式']=phone
#题目(4)
for k,v in msg.items():
    print(k+':'+v)
#题目(5)
li = [11,22,33,22,22,44,55,77,88,99,11]
sli=set(li)
print(len(sli))
#题目(6)
li = [1,2,3,4,5,6,7,8,9]
print(li[2::3])
#题目(7)
s = 'python java php'
print(s[7:12])