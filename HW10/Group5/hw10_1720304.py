
"""
��дһ��Python���򣬲���SQLite���ݿ�ʵ��ͨѶ¼�����ܡ�
����SQLite���ݿ��Ÿ���ͨѶ¼��Ҫ������ϵ�˵��������绰����˾����ַ��
�����Ӧ�ĺ�������������ݿ������
�������ݿ��
������ϵ�ˣ�
��������ѯ��ϵ����ϸ��Ϣ��
ɾ����ϵ�ˣ�
"""

import sqlite3

conn = sqlite3.connect('D:\\xyq.code\\hw10.db')# �������ӵ�һ�����е����ݿ⡣
c = conn.cursor()#������ݿⲻ���ڣ���ô���ͻᱻ��������󽫷���һ�����ݿ����
print("Opened database successfully")
c.execute('''CREATE TABLE USER
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       PHONE         CHAR(15)    NOT NULL,
       COMPANY       CHAR(30)   NOT NULL,
       ADDRESS        CHAR(30)      NOT NULL);''')      # hw10.db �д��� USER ��
print("Table USER created successfully")

# USER ���д�����ϸ��Ϣ
c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (1,'XX', '13585509921', 'A��˾','�½�')")

c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (2,'YY', '13918997878', 'B��˾', '����' )")

c.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (3,'QQ', '13918744128', 'C��˾', '�Ϻ�' )")

conn.execute("INSERT INTO USER (ID,NAME,PHONE,COMPANY,ADDRESS) \
      VALUES (4,'SS', '13547671901', 'D��˾', '�㶫' )")
conn.commit()
print("Insert operation successfully.")

#��ǰ�洴���� USER ���е���connection.execute���������ݿ���в�ѯ����
cursor = c.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS from USER where NAME ='XX' ")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("PASSWORD = ", row[2])
   print("EMAIL = ", row[3])

#����connection.execute���������ݿ����ɾ������
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
EMAIL =  A��˾
Total number of rows deleted : 5
ID =  1
NAME =  XX
PHONE =  13585509921
COMPANY =  A��˾ 

ADDRESS =  �½� 

ID =  3
NAME =  QQ
PHONE =  13918744128
COMPANY =  C��˾ 

ADDRESS =  �Ϻ� 

ID =  4
NAME =  SS
PHONE =  13547671901
COMPANY =  D��˾ 

ADDRESS =  �㶫 

Operation done successfully
"""