
name=input('请输入名字：')
sex=input('请输入性别：')
age=input('请输入年龄：')
info_dict = {}

print(f"我的名字{info_dict['姓名']}，今年{info_dict['年龄']}岁，性别{info_dict['性别']}，喜欢敲代码")

height=input('请输入您的身高：')
tel=input('请输入您的联系方式：')
info_dict['身高']=height
info_dict['联系方式']=tel

for k,v in msg.items():
    print(k+':'+v)

li = [11,22,33,22,22,44,55,77,88,99,11]
sli=set(li)
print(len(sli))

li = [1,2,3,4,5,6,7,8,9]
print(li[2::3])

s = 'python java php'
print(s[7:12])