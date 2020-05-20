
"""
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
创建数据库表；
新增联系人；
按姓名查询联系人详细信息；
删除联系人；
"""

import sqlite3

conn = sqlite3.connect('D:\\xyq.code\\hw10.db')# 尝试连接到一个现有的数据库。
c = conn.cursor()#如果数据库不存在，那么它就会被创建，最后将返回一个数据库对象
print("Opened database successfully")
c.execute('''CREATE TABLE USER
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       PHONE         CHAR(15)    NOT NULL,
       COMPANY       CHAR(30)   NOT NULL,
       ADDRESS        CHAR(30)      NOT NULL);''')      # hw10.db 中创建 USER 表
print("Table USER created successfully")

# USER 表中创建详细信息
c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (1,'XX', '13585509921', 'A公司','新疆')")

c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (2,'YY', '13918997878', 'B公司', '北京' )")

c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (3,'QQ', '13918744128', 'C公司', '上海' )")

conn.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (4,'SS', '13547671901', 'D公司', '广东' )")
conn.commit()
print("Insert operation successfully.")

#从前面创建的 USER 表中调用connection.execute方法在数据库表中查询数据
cursor = c.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS from USER where NAME ='XX' ")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("PASSWORD = ", row[2])
   print("EMAIL = ", row[3])

#调用connection.execute方法在数据库表中删除数据
c.execute("DELETE from USER where ID=2;")
conn.commit()
print("Total number of rows deleted :", conn.total_changes)
cursor = conn.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS  from USER")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("PHONE = ", row[2])
   print("COMPANY = ", row[3], "\n")
   print("ADDRESS = ", row[4], "\n")
print("Operation done successfully")
conn.close()


"""
C:\Users\Administrator\PycharmProjects\untitled\venv\Scripts\python.exe D:/xyq.code/untitled/hw10.py
Opened database successfully
Table USER created successfully
Insert operation successfully.
ID =  1
NAME =  XX
PASSWORD =  13585509921
EMAIL =  A公司
Total number of rows deleted : 5
ID =  1
NAME =  XX
PHONE =  13585509921
COMPANY =  A公司 

ADDRESS =  新疆 

ID =  3
NAME =  QQ
PHONE =  13918744128
COMPANY =  C公司 

ADDRESS =  上海 

ID =  4
NAME =  SS
PHONE =  13547671901
COMPANY =  D公司 

ADDRESS =  广东 

Operation done successfully
"""