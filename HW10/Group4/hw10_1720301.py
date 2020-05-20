'''
    编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
    v采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
    v设计相应的函数完成以下数据库操作：
    n创建数据库表；
    n新增联系人；
    n按姓名查询联系人详细信息；
    n删除联系人；
'''

import sqlite3

conn = sqlite3.connect('1720301.db')  # 数据库连接
print("数据库连接成功！")
cursor = conn.cursor()


#   创建数据库表
def CreateTable():
    try:
        conn.execute('''CREATE TABLE USER
        (ID INT PRIMARY KEY NOT NULL,
        name CHAR(20) NOT NULL,
        tel CHAR(11) NOT NULL,
        company CHAR(50) NOT NULL,
        address CHAR(50));''')
        print("Table USER created successfully")
    except:
        print("此表已存在")


CreateTable()


while True:
    print("")
    print("=" * 31)
    print("="*6,"欢迎使用线人管理系统","="*6)
    print("=" * 31)
    print("1.增加新的线人")
    print("2.查询所有线人")
    print("3.根据线人姓名查找手机号")
    print("d.删除线人")
    print("q.退出")
    print("="*31)
    a = input("请选择要执行的项目：")

    if a == "1":
        try:
            ID = int(input("请输入ID号："))
            name = input("请输入线人姓名：")
            tel = input("请输入手机号：")
            company = input("请输入公司：")
            address = input("请输入地址：")
            sql1 = 'insert into USER(ID,name,tel,company,address)'
            sql1 += 'values("%d","%s","%s","%s","%s");' % (ID,name,tel,company,address)
            conn.execute(sql1)
            conn.commit()
            print("已存入新的线人")
        except:
            print("线人已存在")

    elif a == "2":
        try:
            cursor.execute("SELECT ID,name,tel,company,address From user;")
            userall = cursor.fetchall()
            print(userall)
        except:
            print("查询失败")

    elif a == "3":
        try:
            name = input("请输入要查询的线人: ")
            cursor.execute("SELECT ID,name,tel,company,address From user WHERE name=?;", (name,))
            user = cursor.fetchone()
            print("查询线人:")
            print(user)
        except:
            print("查询失败")

    elif a == "d":
        try:
            delname = input("请输入想要除掉的线人：")
            conn.execute("delete from user where name=?;", (delname,))
            conn.commit()
            print("线人已除")
        except:
            print("无法除去")

    elif a == "q":
        print("再见！")
        break
    else:
        print("您的输入有误")

cursor.close()
conn.close()