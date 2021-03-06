#encoding=utf8
'''

编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
n创建数据库表；
n新增联系人；
n按姓名查询联系人详细信息；
n删除联系人；
'''
import sqlite3# 创建打开数据库，存储联系人的信息

from pip._vendor.distlib.compat import raw_input

conn = sqlite3.connect('1720316zj.db')


conn.execute('''CREATE TABLE USER
      (ID INT PRIMARY KEY     NOT NULL,
    NAME           TEXT    NOT NULL,
      PHONE       TEXT     NOT NULL,
       COMPANY      CHAR(50),
      ADDRESS         CHAR(50));''')
print("Table created successfully")
conn.close()

def Add(): # 增加联系人
    ID = input('请输入联系人id号:\n')
    NAME = raw_input('请输入联系人名称:\n')
    PHONE = input('请输入手机号码:\n')
    COMPANY = raw_input('请输入联系人公司:\n')
    ADDRESS = input('请输入联系人地址:\n')
    sql1 = 'insert into USER(ID,NAME,PHONE,COMPANY,ADDRESS)'
    sql1 += 'values("%s","%s","%s","%s","%s");' % (ID, NAME, PHONE, COMPANY, ADDRESS)
    conn.execute(sql1)
    conn.commit()
    print("添加成功！")



conn = sqlite3.connect('1720316zj.db')


def Chaxun():# 查询联系人信息
    conn = sqlite3.connect('1720316zj.db')
    name = raw_input('请输入要查询的联系人姓名：')
    sql2 = "SELECT ID,NAME,PHONE,COMPANY,ADDRESS from USER where name= '%s';" % (name)
    cursor = conn.execute(sql2)
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("PHONE = ", row[2])
        print("COMPANY = ", row[3])
        print("ADDRESS = " "\n")
        break
    else:
        print("输入错误!没有该联系人！")

def Delete():# 删除联系人信息
    name = raw_input("请输入所要删除的联系人姓名:")
    cursor = conn.execute("SELECT name from USER where name = '%s';" % name)
    for row in cursor:
        if name == row[0]:
            conn.execute("DELETE from USER where name = '%s';" % name)
            conn.commit()
            print("删除联系人成功！")
            break
    else:
        print("对不起输入错误!没有该联系人！")

def Xiuzheng():# 修改联系人的信息
    name = raw_input("请输入要修改的联系人姓名:")
    sql3 = "SELECT ID, NAME, PHONE,COMPANY, ADDRESS from USER where name = '%s';" % name
    cursor = conn.execute(sql3)
    x = raw_input("请输入联系人手机号码:")
    y = input("请输入联系人公司:")
    z = input("请输入联系人地址:")
    sql4 = "UPDATE USER set PHONE = '%s',COMPANY = '%s',\
        ADDRESS = '%s' where name = '%s';" % (x, y, z, name)
    conn.execute(sql4)
    conn.commit()
    print("修改成功!")
    sql5 = "SELECT ID, NAME, PHONE,COMPANY, ADDRESS  from USER where name = '%s';" % name
    cursor = conn.execute(sql5)
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("PHONE = ", row[2])
        print("COMPANY = ", row[3])
        print("ADDRESS = ", row[4], "\n")

def show():# 显示联系人信息
    cursor = conn.execute("SELECT ID, NAME, PHONE,COMPANY, ADDRESS  from USER")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("PHONE = ", row[2])
        print("COMPANY = ", row[3])
        print("ADDRESS = ", row[4], "\n")
    cursor = conn.execute("select count(*) from USER;")
    for row in cursor:
        print("当前共有%d个用户" % row[0])

def menu():# 菜单列表选项
    print('1.新增联系人')
    print('2.查询联系人')
    print('3.删除联系人')
    print('4.修改联系人')
    print('5.显示所有联系人')


while True:
    menu()
    x = raw_input('请输入您想要操作的编号:')
    if x == '1':
        Add()
        continue
    if x == '2':
        Chaxun()
        continue
    if x == '3':
        Delete()
        continue
    if x == '4':
        Xiuzheng()
        continue
    if x == '5':
        show()
        continue
    else:
        print("输入错误，请重新输入！")
        continue