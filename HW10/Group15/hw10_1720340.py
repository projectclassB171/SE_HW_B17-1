'''
1720340 李昀燕 HW10
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
n创建数据库表；
n新增联系人；
n按姓名查询联系人详细信息；
n删除联系人；
'''

import sqlite3

conn = sqlite3.connect('1720340.db')
c = conn.cursor()


def 建库表1720340():
    global conn
    sql = (
        "CREATE TABLE LYY(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,COMPANY INT CHAR(50),ADDRESS CHAR(50),TELENUMBER TEXT);")
    conn.execute(sql)
    conn.commit()


建库表1720340()


def add():
    global conn
    c = conn.cursor()
    ID = int(input("请输入ID号："))
    name = input("请输入姓名：")
    company = input("请输入公司：")
    address = input("请输入地址：")
    telenumber = input("请输入电话号码:")
    sql1 = 'insert into LYY(ID,NAME,COMPANY,ADDRESS,TELENUMBER)'
    sql1 += 'values("%d","%s","%s","%s","%s");' % (ID, name, company, address, telenumber)
    conn.execute(sql1)
    conn.commit()
    print("用户信息提交完成")


def delete():
    global conn
    c = conn.cursor()
    i = input("请输入所要删除的联系人姓名或电话号码:")
    if len(i) < 11:
        cursor = c.execute("SELECT name from LYY where name = '%s';" % i)
        for row in cursor:
            if i == row[0]:
                c.execute("DELETE from LYY where name ='%s';" % i)
                conn.commit()
                print("已成功删除联系人信息！")
                break
        else:
            print("输入姓名有误，该联系人不存在，请重新输入！")
    else:
        cursor = c.execute("SELECT name from LYY where telenumber= '%s';" % i)
        for row in cursor:
            if i == row[0]:
                c.execute("DELETE from LYY where telenumber ='%s';" % i)
                conn.commit()
                print("成功删除联系人信息！")
                break
        else:
            print("电话号码有误，该联系人不存在，请重新输入！")


def select():
    global conn
    c = conn.cursor()
    name = input("请输入所要查询的联系人姓名:")
    sql2 = "SELECT id,name,company, address, telenumber from LYY where name = '%s';" % (name)
    cursor = c.execute(sql2)
    for row in cursor:
        print("id:{0}".format(row[0]))
        print("姓名:{0}".format(row[1]))
        print("公司:{0}".format(row[2]))
        print("地址:{0}".format(row[3]))
        print("电话号码:{0}".format(row[4]))
        break
    else:
        print("没有查找到该联系人，请查证后重新输入！")




print("==本通讯录相关操作指令如下：==\n1.输入\"新增\"添加联系人信息\n2.输入\"删除\"删除指定联系人 \n3.输入\"查询\"根据姓名查询 ")
while 1:
    temp = input("请输入操作指令：")
    if temp == "新增":
        add()
        print("添加成功！")
        temp1 = input("是否继续操作通讯录？(请输入：是 或 否)")
        if temp1 == "否":
            print("退出成功！")
            break
        else:
            continue
    elif temp == "删除":
        delete()
        temp1 = input("是否继续操作通讯录？(请输入：是 或 否)")
        if temp1 == "否":
            print("退出成功！")
            break
        else:
            continue
    elif temp == "查询":
        select()
        temp1 = input("是否继续添加？(请输入：是 或 否)")
        if temp1 == "否":
            print("退出成功！")
            break
        else:
            continue
    else:
        print("输入指令不正确，请重新输入")
conn.close()
