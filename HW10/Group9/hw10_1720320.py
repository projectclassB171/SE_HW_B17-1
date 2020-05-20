#编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
#采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
#设计相应的函数完成以下数据库操作：
#创建数据库表；
#新增联系人；
#按姓名查询联系人详细信息；
#删除联系人；

import sqlite3
conn = sqlite3.connect('1720320.db')
c = conn.cursor()
print("Opened database successfully.")

def create():#创建数据库表的函数
    global conn
    sql = ("CREATE TABLE person_1720320(NAME TEXT NOT NULL,TEL INT NOT NULL,COMPANY TEXT CHAR(50),ADDR CHAR(50));")
    conn.execute(sql)
    conn.commit()
def insert():#插入用户信息的函数
    global conn
    c = conn.cursor()
    iNAME=input("姓名：")
    iTEL= input("电话号码:")
    iCOMPANY=input("公司：")
    iADDR=input("地址：")
    user=(iNAME,iTEL,iCOMPANY,iADDR)
    c.execute("INSERT INTO person_1720320 (NAME,TEL,COMPANY,ADDR) \
    VALUES (?,?,?,?)",user)
    conn.commit()
    print("Insert operation successfully.")

def select():#查询用户信息的函数
    global conn
    c = conn.cursor()
    sNAME=input("请输入要查询联系人姓名:")
    c.execute("SELECT NAME,TEL,COMPANY,ADDR from person_1720320 WHERE NAME = ?;", (sNAME,))
    print(c.fetchall())
    print("Select operation successfully.")

def delete():#删除用户信息的函数
    global conn
    c = conn.cursor()
    dNAME = input("请输入要删除联系人姓名：")
    c.execute("DELETE from person_1720320 WHERE NAME = ?;", (dNAME,))
    conn.commit()
    print("Delete operation successfully.")
    conn.close()


if __name__ == '__main__':
  create()
  insert()
  select()
  delete()


运行结果：
D:\pytest\venv\Scripts\python.exe D:/pytest/项目实战/SQL.py
Opened database successfully.
姓名：王震杰
电话号码:13819333979
公司：腾讯公司
地址：深圳
Insert operation successfully.
请输入要查询联系人姓名:王震杰
[('王震杰', 13819333979, '腾讯公司', '深圳')]
Select operation successfully.
请输入要删除联系人姓名：王震杰
Delete operation successfully.

Process finished with exit code 0
