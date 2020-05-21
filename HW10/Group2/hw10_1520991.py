'''
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
创建数据库表；
新增联系人；
按姓名查询联系人详细信息；
删除联系人；

'''

import sqlite3
conn=sqlite3.connect('1520991.db')
print("连接数据库成功！")
cursor = conn.cursor()

try:
    conn.execute('''CREATE TABLE USER
    (id INT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    phone CHAR(11) NOT NULL,
    company VARCHAR(100) NOT NULL,
    address VARCHAR(100));''')
    print("创建数据表成功！")
except:
    print("数据表已存在\n")

#添加信息
try:
    id = int(input('请输入ID: '))
    name = str(input('请输入名字: '))
    phone = str(input('请输入手机号: '))
    company = str(input('请输入公司: '))
    address = str(input('请输入地址: '))
    sql = "insert into user(id,name,phone,company,address) values(?,?,?,?,?)"
    cursor.execute(sql, (id, name, phone, company, address))
    conn.commit()
    print("添加成功")
    conn.rollback()
except:
    print("添加失败")

#查询信息
try:
    name = input("请输入查询的姓名")
    cursor.execute("SELECT * From user WHERE name=?;", (name,))
    print("结果为",cursor.fetchone())
except:
    print("输入有误！\n")

#删除信息
try:
    id=int(input('请输入删除的id： '))
    conn.execute("delete from user where ID=?;",(id,))
    conn.commit()
    print("删除成功！")
except:
    print("删除失败！")