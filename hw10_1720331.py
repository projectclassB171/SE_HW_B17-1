# coding=gbk
'''
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
n创建数据库表；
n新增联系人；
n按姓名查询联系人详细信息；
n删除联系人；

'''

import sqlite3
conn = sqlite3.connect('1720331.db')
print("数据库创建成功！.")
c = conn.cursor()

#创建数据库表
def create():
    global conn
    sql = ("CREATE TABLE person_1720331(NAME TEXT NOT NULL,TEL INT NOT NULL,COMPANY TEXT CHAR(100),ADDR CHAR(100));")
    conn.execute(sql)
    conn.commit()
    create()
#插入用户信息
def insert():
    global conn
    c = conn.cursor()
    id_NAME=input("姓名：")
    id_TEL= input("电话号码:")
    id_COMPANY=input("公司：")
    id_ADDR=input("地址：")
    user=(id_NAME,id_TEL,id_COMPANY,id_ADDR)
    c.execute("INSERT INTO person_1720331 (NAME,TEL,COMPANY,ADDR) \
    VALUES (?,?,?,?)",user)
    conn.commit()
    print("信息插入成功！.")
    
insert()
    
#查询用户信息
def select():
    global conn
    c = conn.cursor()
    sNAME=input("输入要查询联系人姓名:")
    c.execute("SELECT NAME,TEL,COMPANY,ADDR from person_1720331 WHERE NAME = ?;", (sNAME,))
    print(c.fetchall())
    print("信息查询成功.")
    
select()

#删除用户信息的函数
def delete():
    global conn
    c = conn.cursor()
    dNAME = input("输入要删除联系人姓名：")
    c.execute("DELETE from person_1720331 WHERE NAME = ?;", (dNAME,))
    conn.commit()
    print("信息删除成功！.")
    conn.close()
    
delete()

