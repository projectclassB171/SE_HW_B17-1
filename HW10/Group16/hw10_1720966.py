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
conn = sqlite3.connect('D:\\tools\\untitled\\hw10_1720966.db')# 创建一个hw10_1720966.db数据库
print("连接数据库hw10_1720966.db成功");
cursor = conn.cursor()  # 创建游标

#创建数据库表id主键，姓名、电话、公司、地址；
def create():
    try:
        conn.execute('''CREATE TABLE PhoneCall (
                        ID            INT   PRIMARY KEY     NOT NULL, 
                        NAME          TEXT    NOT NULL, 
                        PHONE         INT     NOT NULL,
                        COMPANY       TEXT     NOT NULL, 
                        ADDRESS       TEXT     NOT NULL 
                        );''')
        print("数据表PhoneCall创建成功！");
    except:
        print("数据表PhoneCall已存在!")

#新增联系人
def insert():
    ID = input('请输入联系人ID号:')
    NAME = input('请输入联系人名字:')
    PHONE = input('请输入联系人手机号码:')
    COMPANY = input('请输入联系人公司:')
    ADDRESS = input('请输入联系人地址:')
    try:
        conn.execute("INSERT INTO PhoneCall (ID,NAME,PHONE,COMPANY,ADDRESS)  VALUES ('%s', '%s', '%s', '%s', '%s')" %(ID, NAME, PHONE, COMPANY, ADDRESS ))
        conn.commit()
        print('添加联系人成功！')
    except:
        print("ID已存在!")

#按姓名查询联系人详细信息；
def select():
    NAME = input('请输入所要查询的联系人名字:')
    cursor = conn.execute("SELECT ID,NAME,PHONE,COMPANY,ADDRESS from PhoneCall where NAME='%s'" %(NAME))
#	cursor.fetchone()该方法获取查询结果集中的下一行，返回一个单一的序列，当没有更多可用的数据时，则返回 None。
    lxr = cursor.fetchone()
    print("联系人详细信息是：", lxr)


#删除联系人；
def delete():
    ID = input('请输入所要删除的联系人ID:')
    try:
        conn.execute("delete from PhoneCall where ID='%s'" %(ID))
        conn.commit()
        print("已经删除联系人ID：", ID)
    except:
        print("不存在该联系人")


# 菜单列表选项
def menu():
    print('1.新增联系人')
    print('2.查询联系人')
    print('3.删除联系人')
    print('4.结束操作')

create()
while True:
    menu()
    a = input('请输入您想要操作的编号:')
    if a == '1':
        insert()
        continue
    if a == '2':
        select()
        continue
    if a == '3':
        delete()
        continue
    if a == '4':
        break
    else:
        print("输入错误，请重新输入！")
        continue