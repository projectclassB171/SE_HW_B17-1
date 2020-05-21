# ��дһ��Python���򣬲���SQLite���ݿ�ʵ��ͨѶ¼�������ܡ�
# v����SQLite���ݿ��Ÿ���ͨѶ¼��Ҫ������ϵ�˵��������绰����˾����ַ��
# v�����Ӧ�ĺ�������������ݿ������
# n�������ݿ����
# n������ϵ�ˣ�
# n��������ѯ��ϵ����ϸ��Ϣ��
# nɾ����ϵ�ˣ�

import sqlite3

# ���������ݿ⣬�洢��ϵ�˵���Ϣ
from pip._vendor.distlib.compat import raw_input

conn = sqlite3.connect('people.db')


conn.execute('''CREATE TABLE USER
      (ID INT PRIMARY KEY     NOT NULL,
    NAME           TEXT    NOT NULL,
      PHONE       TEXT     NOT NULL,
       COMPANY      CHAR(50),
      ADDRESS         CHAR(50));''')
print("Table created successfully")
conn.close()


# ������ϵ��
def insert():
    ID = input('��������ϵ��id��:\n')
    NAME = raw_input('��������ϵ������:\n')
    PHONE = input('�������ֻ�����:\n')
    COMPANY = raw_input('��������ϵ�˹�˾:\n')
    ADDRESS = input('��������ϵ�˵�ַ:\n')
    sql1 = 'insert into USER(ID,NAME,PHONE,COMPANY,ADDRESS)'
    sql1 += 'values("%s","%s","%s","%s","%s");' % (ID, NAME, PHONE, COMPANY, ADDRESS)
    conn.execute(sql1)
    conn.commit()
    print("���ӳɹ���")


# ��ѯ��ϵ��
conn = sqlite3.connect('people.db')


def query():
    conn = sqlite3.connect('people.db')
    name = raw_input('������Ҫ��ѯ����ϵ��������')
    sql2 = "SELECT ID,NAME,PHONE,COMPANY,ADDRESS from USER where name= '%s';" % (name)
    cursor = conn.execute(sql2)
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("PHONE = ", row[2])
        print("COMPANY = ", row[3])
        print("ADDRESS = ", row[4], "\n")
        break
    else:
        print("�������!û�и���ϵ�ˣ�")



# ɾ����ϵ��
def delete():
    name = raw_input("��������Ҫɾ������ϵ������:")
    cursor = conn.execute("SELECT name from USER where name = '%s';" % name)
    for row in cursor:
        if name == row[0]:
            conn.execute("DELETE from USER where name = '%s';" % name)
            conn.commit()
            print("ɾ����ϵ�˳ɹ���")
            break
    else:
        print("�������!û�и���ϵ�ˣ�")




# �޸���ϵ�˵���Ϣ

def change():
    name = raw_input("������Ҫ�޸ĵ���ϵ������:")
    sql3 = "SELECT ID, NAME, PHONE,COMPANY, ADDRESS from USER where name = '%s';" % name
    cursor = conn.execute(sql3)
    x = raw_input("��������ϵ���ֻ�����:")
    y = input("��������ϵ�˹�˾:")
    z = input("��������ϵ�˵�ַ:")
    sql4 = "UPDATE USER set PHONE = '%s',COMPANY = '%s',\
        ADDRESS = '%s' where name = '%s';" % (x, y, z, name)
    conn.execute(sql4)
    conn.commit()
    print("�޸ĳɹ�!")
    sql5 = "SELECT ID, NAME, PHONE,COMPANY, ADDRESS  from USER where name = '%s';" % name
    cursor = conn.execute(sql5)
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("PHONE = ", row[2])
        print("COMPANY = ", row[3])
        print("ADDRESS = ", row[4], "\n")



# ��ʾ������ϵ����Ϣ
def showall():
    cursor = conn.execute("SELECT ID, NAME, PHONE,COMPANY, ADDRESS  from USER")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("PHONE = ", row[2])
        print("COMPANY = ", row[3])
        print("ADDRESS = ", row[4], "\n")
    cursor = conn.execute("select count(*) from USER;")
    for row in cursor:
        print("��ǰ����%d���û�" % row[0])


# �˵��б�ѡ��
def menu():
    print('1.������ϵ��')
    print('2.��ѯ��ϵ��')
    print('3.ɾ����ϵ��')
    print('4.�޸���ϵ��')
    print('5.��ʾ������ϵ��')


while True:
    menu()
    x = raw_input('����������Ҫ����ǰ�ı��:')
    if x == '1':
        insert()
        continue
    if x == '2':
        query()
        continue
    if x == '3':
        delete()
        continue
    if x == '4':
        change()
        continue
    if x == '5':
        showall()
        continue
    else:
        print("����������������룡")
        continue