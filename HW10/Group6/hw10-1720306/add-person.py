import sqlite3

from person import Person

conn = sqlite3.connect("test.db")
list1 = []
ID =input('请输入id：')
name = input('请输入您的姓名：')
tel = input('请输入您的电话：')
company = input('请输入您的公司：')
address = input('请输入您的地址：')
EMAIL = input('请输入e-mail：')
per = Person(ID,name,tel,company,address,EMAIL)
if per in list1:
    print('已存在该联系人！')
else:
    list1.append(per)

for per in list1:
    conn.execute("insert into USER11 (ID,NAME,TEL,COMPANY,ADDRESS,EMAIL)" 
                 "values('%s','%s', '%s', '%s', '%s','%s')"
                 % (per.ID,per.NAME, per.TEL,per.COMPANY,per.ADDRESS,per.EMAIL))
    print(f'添加成功')
conn.commit()