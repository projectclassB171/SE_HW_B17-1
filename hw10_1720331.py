# coding=gbk
'''
��дһ��Python���򣬲���SQLite���ݿ�ʵ��ͨѶ¼�����ܡ�
����SQLite���ݿ��Ÿ���ͨѶ¼��Ҫ������ϵ�˵��������绰����˾����ַ��
�����Ӧ�ĺ�������������ݿ������
n�������ݿ��
n������ϵ�ˣ�
n��������ѯ��ϵ����ϸ��Ϣ��
nɾ����ϵ�ˣ�

'''

import sqlite3
conn = sqlite3.connect('1720331.db')
print("���ݿⴴ���ɹ���.")
c = conn.cursor()

#�������ݿ��
def create():
    global conn
    sql = ("CREATE TABLE person_1720331(NAME TEXT NOT NULL,TEL INT NOT NULL,COMPANY TEXT CHAR(100),ADDR CHAR(100));")
    conn.execute(sql)
    conn.commit()
    create()
#�����û���Ϣ
def insert():
    global conn
    c = conn.cursor()
    id_NAME=input("������")
    id_TEL= input("�绰����:")
    id_COMPANY=input("��˾��")
    id_ADDR=input("��ַ��")
    user=(id_NAME,id_TEL,id_COMPANY,id_ADDR)
    c.execute("INSERT INTO person_1720331 (NAME,TEL,COMPANY,ADDR) \
    VALUES (?,?,?,?)",user)
    conn.commit()
    print("��Ϣ����ɹ���.")
    
insert()
    
#��ѯ�û���Ϣ
def select():
    global conn
    c = conn.cursor()
    sNAME=input("����Ҫ��ѯ��ϵ������:")
    c.execute("SELECT NAME,TEL,COMPANY,ADDR from person_1720331 WHERE NAME = ?;", (sNAME,))
    print(c.fetchall())
    print("��Ϣ��ѯ�ɹ�.")
    
select()

#ɾ���û���Ϣ�ĺ���
def delete():
    global conn
    c = conn.cursor()
    dNAME = input("����Ҫɾ����ϵ��������")
    c.execute("DELETE from person_1720331 WHERE NAME = ?;", (dNAME,))
    conn.commit()
    print("��Ϣɾ���ɹ���.")
    conn.close()
    
delete()

