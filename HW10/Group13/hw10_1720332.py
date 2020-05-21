import sqlite3
conn = sqlite3.connect('1720332.db')
print("Opened database successfully.")
c = conn.cursor()

#创建数据库表函数
def create():
    global conn
    sql = ("CREATE TABLE person_1720332(NAME TEXT NOT NULL,TEL INT NOT NULL,COMPANY TEXT CHAR(100),ADDR CHAR(100));")
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
    c.execute("INSERT INTO person_1720332 (NAME,TEL,COMPANY,ADDR) \
    VALUES (?,?,?,?)",user)
    conn.commit()
    print("Insert operation successfully.")
    
insert()
    
#查询用户信息
def select():
    global conn
    c = conn.cursor()
    sNAME=input("输入要查询联系人姓名:")
    c.execute("SELECT NAME,TEL,COMPANY,ADDR from person_1720332 WHERE NAME = ?;", (sNAME,))
    print(c.fetchall())
    print("信息查询成功.")
    
select()

#删除用户信息的函数
def delete():
    global conn
    c = conn.cursor()
    dNAME = input("输入要删除联系人姓名：")
    c.execute("DELETE from person_1720332 WHERE NAME = ?;", (dNAME,))
    conn.commit()
    print("Delete operation successfully.")
    conn.close()
    
delete()