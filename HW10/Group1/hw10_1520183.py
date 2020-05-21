'''
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
    创建数据库表；
    新增联系人；
    按姓名查询联系人详细信息；
    删除联系人；
'''
import sqlite3   #导入sqlite3模块
conn = sqlite3.connect('C:\\Users\\Yan\\Desktop\\hw10_1520183.db') #调用connect函数连接SQLite数据库，得到连接对象hw10_1520183.db
print("连接数据库hw10_1520183.db成功");
cursor = conn.cursor()  # 创建游标对象cur

#调用connection.execute方法创建数据库表
def create():
    try:
        conn.execute('''CREATE TABLE addressList
(NAME          TEXT     NOT NULL, 
 TEL           INT      NOT NULL,
 COMPANY       TEXT     NOT NULL, 
 ADDRESS       TEXT     CHAR(50));''')
        print("通讯录创建成功！");
    except:
        print("通讯录已存在！")

#调用connection.execute方法在数据库表中插入数据
def insert():
    NAME = input('姓名:')
    TEL = input('电话:')
    COMPANY = input('公司:')
    ADDRESS = input('地址:')
    sql1 = 'insert into addressList(NAME,TEL,COMPANY,ADDRESS)'
    sql1 += 'values("%s","%s","%s","%s");' % (NAME,TEL,COMPANY,ADDRESS)
    conn.execute(sql1)
    conn.commit()
    print("添加成功！")

#调用connection.execute方法在数据库表中查询数据
def select():
    NAME = input("请输入联系人姓名:") #按姓名查询联系人详细信息
    cursor = conn.execute("SELECT NAME,TEL,COMPANY,ADDRESS from addressList where NAME='%s'" %(NAME)) #使用execute方法获得游标(cursor)对象
    n = cursor.fetchone()   #利用游标对象的fetchone()方法返回一条记录从而获得查询结果，如果没有结果则返回 None
    print("查询成功：", n)


#调用connection.execute方法在数据库表中删除数据
def delete():
    NAME = input("请输入联系人姓名:")
    try:
        conn.execute("delete from addressList where NAME='%s'" %(NAME))
        conn.commit()
        print("删除成功！")
    except:
        print("联系人不存在！")


#功能选项
def option():
    print('新增联系人请扣1')
    print('查询联系人请扣2')
    print('删除联系人请扣3')
    print('结束操作请扣4')

create()
while True:
    option()
    o = input('请输入数字:')
    if o == '1':
        insert()
        continue
    if o == '2':
        select()
        continue
    if o == '3':
        delete()
        continue
    if o == '4':
        break
    else:
        print("输入有误，请重新输入！")
        continue

= RESTART: D:/Users/Yan/AppData/Local/Programs/Python/Python38-32/hw10_1520183.py
连接数据库hw10_1520183.db成功
通讯录创建成功！
新增联系人请扣1
查询联系人请扣2
删除联系人请扣3
结束操作请扣4
请输入数字:我
输入有误，请重新输入！
新增联系人请扣1
查询联系人请扣2
删除联系人请扣3
结束操作请扣4
请输入数字:1
姓名:龙五
电话:186
公司:剑桥
地址:尚海
添加成功！
新增联系人请扣1
查询联系人请扣2
删除联系人请扣3
结束操作请扣4
请输入数字:2
请输入联系人姓名:龙五
查询成功： ('龙五', 186, '剑桥', '尚海')
新增联系人请扣1
查询联系人请扣2
删除联系人请扣3
结束操作请扣4
请输入数字:2
请输入联系人姓名:龙
查询成功： None
新增联系人请扣1
查询联系人请扣2
删除联系人请扣3
结束操作请扣4
请输入数字:3
请输入联系人姓名:龙五
删除成功！
新增联系人请扣1
查询联系人请扣2
删除联系人请扣3
结束操作请扣4
请输入数字:4
>>> 