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

conn = sqlite3.connect('1720314.db')  # 数据库连接
print("连接成功！")
cursor = conn.cursor()


#   创建数据库表
def CreateTable():
    try:
        conn.execute('''CREATE TABLE USER
        (ID INT PRIMARY KEY NOT NULL,
        name CHAR(50) NOT NULL,
        tel CHAR(11) NOT NULL,
        company CHAR(100) NOT NULL,
        address CHAR(100));''')
        print("表已创建")
    except:
        print("此表已存在")


CreateTable()


while True:
  
    print("=" * 31)
    print("1.增加新的联系人")
    print("2.查询所有联系人"）
    print("3.删除联系人")
    print("4.退出")
    a = input("请选择序号：")

    if a == "1":
        try:
            ID = int(input("请输入ID号："))
            name = input("请输入姓名：")
            tel = input("请输入手机号：")
            company = input("请输入公司：")
            address = input("请输入地址：")
            sql1 = 'insert into USER(ID,name,tel,company,address)'
            sql1 += 'values("%d","%s","%s","%s","%s");' % (ID,name,tel,company,address)
            conn.execute(sql1)
            conn.commit()
            print("已存入！")
        except:
            print("已存在！")

    elif a == "2":
        try:
            cursor.execute("SELECT ID,name,tel,company,address From user;")
            userall = cursor.fetchall()
            print(userall)
        except:
            print("查询失败！")

    elif a == "3":
        try:
            delname = input("请输入想要删除的联系人：")
            conn.execute("delete from user where name=?;", (name,))
            conn.commit()
            print("已删除！")
        except:
            print("无法删除！")

    elif a == "4":
        print("退出！")
        break
    else:
        print("输入有误！")
