'''
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
n创建数据库表；
n新增联系人；
n按姓名查询联系人详细信息；
n删除联系人；

'''
import sqlite3

conn = sqlite3.connect('1720334.db')#数据库连接
c = conn.cursor()

def 先建库表1720334XX():#创建数据库表的函数
    global conn
    sql = ("CREATE TABLE XX(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,GS INT CHAR(50),ADDRESS CHAR(50),TELENUMBER TEXT);")
    conn.execute(sql)
    conn.commit()#提交当前的事务


    
先建库表1720334XX() #请在代码首次执行成功后注释 “先建库表1720334XX()”,防止重复创建导致报错



def 添加():#增加用户信息
    global conn
    c = conn.cursor()
    ID=int(input("请输入ID号："))
    name=input("请输入姓名：")
    gs=input("请输入公司：")
    address=input("请输入地址：")
    telenumber=input("请输入电话号码(不要超过11位):")#涉及删除时的判断条件
    sql1 = 'insert into XX(ID,NAME,GS,ADDRESS,TELENUMBER)'
    sql1 += 'values("%d","%s","%s","%s","%s");' % (ID,name, gs, address, telenumber)
    conn.execute(sql1)
    conn.commit()#提交，否则无法保存
    print("用户信息提交完成")

def 删除():#删除用户信息
    global conn
    c=conn.cursor()
    i = input("请输入所要删除的联系人姓名或电话号码:")
    if len(i) < 11:#是否满足11位
        cursor = c.execute("SELECT name from XX where name = '%s';"%i)
        for row in cursor:
            if i == row[0]:
                c.execute("DELETE from XX where name ='%s';"%i)
                conn.commit()
                print("成功删除联系人信息！")
                break
        else:
            print("姓名有误！该联系人不存在！")
    else :
        cursor = c.execute("SELECT name from XX where telenumber= '%s';" % i)
        for row in cursor:
            if i == row[0]:
                c.execute("DELETE from XX where telenumber ='%s';" % i)
                conn.commit()
                print("成功删除联系人信息！")
                break
        else:
            print("电话号码错误！该联系人不存在！")

def 查询():#查询用户信息（按姓名查询）
    global conn
    c = conn.cursor()
    name = input("请输入所要查询的联系人姓名:")
    sql2 = "SELECT id,name,gs, address, telenumber from XX where name = '%s';" % (name) 
    cursor = c.execute(sql2)
    for row in cursor:
        print("id:{0}".format(row[0]))
        print("姓名:{0}".format(row[1]))
        print("年龄:{0}".format(row[2]))
        print("地址:{0}".format(row[3]))
        print("电话号码:{0}".format(row[4]))
        break
    else:
        print("查无此人！")    

def 显示():#显示所有用户信息(便于查看)
    global conn
    c = conn.cursor()
    cursor = c.execute("SELECT id, name, gs, address, telenumber  from XX")
    for row in cursor:
        print("id:{0}".format(row[0]))
        print("姓名:{0}".format(row[1]))
        print("公司:{0}".format(row[2]))
        print("地址:{0}".format(row[3]))
        print("电话号码:{0}".format(row[4]))
print("==请输入以下指令：==\n1.输入\"添加\"添加联系人信息\n2.输入\"删除\"删除指定联系人 \n3.输入\"显示\"显示所有联系人信息 \n4.输入\"查询\"根据姓名查询 ")
while 1:
    temp = input("请输入操作指令：")
    if temp == "添加":
        添加()
        print("添加成功！")
        temp1=input("是否继续操作通讯录？(请输入：Yes 或 No)")
        if temp1=="No":
            print("退出成功！")
            break
        else:
            continue
    elif temp=="删除":
        删除()
        temp1 = input("是否继续操作通讯录？(请输入：Yes 或 No)")
        if temp1 == "No":
            print("退出成功！")
            break
        else:
            continue
    elif temp=="显示":
        显示()
        temp1 = input("是否想继续操作通讯录？(请输入：Yes 或 No)")
        if temp1 == "No":
            print("退出成功！")
            break
        else:
            continue
    elif temp=="查询":
        查询()
        temp1 = input("是否想继续操作通讯录？(请输入：Yes 或 No)")
        if temp1 == "No":
            print("退出成功！")
            break
        else:
            continue           
    else:
        print("请重新输入正确指令！！！")
conn.close()#关闭数据库

