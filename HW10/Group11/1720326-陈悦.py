#coding=utf-8
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
conn = sqlite3.connect('mysql_telephone_book.db')# 创建一个数据库
print("连接数据库成功");
cursor = conn.cursor()  # 创建游标

#创建数据库表
def create():
    try:
        conn.execute('''CREATE TABLE telephone_book(
                        ID            INT   PRIMARY KEY     NOT NULL, 
                        NAME          TEXT    NOT NULL, 
                        TELENUMBER         INT     NOT NULL,
                        COMPANY       TEXT     NOT NULL, 
                        ADDRESS       TEXT     NOT NULL 
                        );''')
        print("数据表telephone_book创建成功！");
    except:
        print("数据表telephone_book已存在!")

#新增联系人信息
def insert():
    ID = input('请输入ID号:')
    NAME = input('请输入名字:')
    TELENUMBER = input('请输入手机号码:')
    COMPANY = input('请输入公司:')
    ADDRESS = input('请输入地址:')
    try:
        conn.execute("INSERT INTO telephone_book (ID,NAME,TELENUMBER,COMPANY,ADDRESS)  VALUES ('%s', '%s', '%s', '%s', '%s')" %(ID, NAME, TELENUMBER, COMPANY, ADDRESS ))
        conn.commit()
        print('添加联系人成功！')
    except:
        print("ID已存在!")

#按姓名查询联系人信息；
def select():
    NAME = input('请输入所要查询的联系人名字:')
    cursor = conn.execute("SELECT ID,NAME,TELENUMBER,COMPANY,ADDRESS from telephone_book where NAME='%s'" %(NAME))
#	cursor.fetchone()返回一个单一的序列   
    lxr = cursor.fetchone()
    print("联系人详细信息是：", lxr)


#删除联系人信息
def delete():
    ID = input('请输入所要删除的联系人ID:')
    try:
        conn.execute("delete from telephone_book where ID='%s'" %(ID))
        conn.commit()
        print("已经删除联系人ID：", ID)
    except:
        print("不存在该联系人")


# 菜单列表选项
def menu():
    print('1.输入\"add\"为通讯录添加联系人信息')
    print('2.输入\"search\"根据姓名查找联系人信息')
    print('3.输入\"delete\"删除通讯录里的指定联系人信息')

create()
while True:
    menu()
    temp = input("请输入指令：")
    if temp == "add":
        insert()
        print("添加成功！")
        temp1=input("是否继续操作通讯录？(y or n)")
        if temp1=="n":
            print("成功退出！！")
            break
        else:
            continue
    elif temp=="delete":
        delete()
        temp1 = input("是否继续操作通讯录？(y or n)")
        if temp1 == "n":
            print("成功退出！！")
            break
        else:
            continue
    elif temp=="search":
        select()
        temp1 = input("您是否想继续操作通讯录？(y or n)")
        if temp1 == "n":
            print("成功退出！！")
            break
        else:
            continue
    else:
        print("请输入正确指令！！")