"""
      编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
      采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
      设计相应的函数完成以下数据库操作：
      n创建数据库表；
      n新增联系人；
      n按姓名查询联系人详细信息；
      n删除联系人；
"""

import sqlite3

conn = sqlite3.connect('persAddrBook.db')  # 创建一个数据库，文件名
print("数据库连接成功!")
cursor = conn.cursor()  # 创建游标


# 创建数据库表UserAddrBook
def table():
    try:
        conn.execute('''CREATE TABLE UserAddrBook
        (id INT PRIMARY KEY NOT NULL,
        name CHAR(20) NOT NULL,
        tel CHAR(11) NOT NULL,
        company CHAR(50) NOT NULL,
        addr CHAR(50) NOT NULL) ;''')
        print("表已创建！")
    except:
        print("数据表已存在\n")


# 新增联系人add()
def add():
    try:
        print("新增个人联络通讯录用户(id不可重复！)\n")
        _id = input("请输入id:")
        _name = input("请输入姓名:")
        _tel = input("请输入电话:")
        _company = input("请输入公司:")
        _addr = input("请输入地址:")
    except:
        print("输入有误,不可進行插入操作！\n")
    else:
        try:

            cursor.execute('''INSERT INTO UserAddrBook (id,name,tel,company,addr) VALUES (?,?,?,?,?)''',
                           (_id, _name, _tel, _company, _addr,))
            conn.commit()  # 提交
            res = conn.total_changes
            print("{0} 行记录已改变 .".format(res))
        except:
            print("请勿插入重复数据!\n")


# 查询所有用户信息select()
def select():
    cursor.execute("SELECT id,name,tel,company,addr FROM UserAddrBook")
    users = cursor.fetchall()  # 返回多条记录(row)
    print(users)


# 按姓名查询联系人详细信息selectName()
def selectName():
    try:
        name = input("请输入要查询的姓名")
        cursor.execute("SELECT id,name,tel,company,addr FROM UserAddrBook WHERE name=?;", (name,))
        user = cursor.fetchone()
        print("查询结果为:")
        print(user)

    except:
        print("输入有误,跳过查询\n")


# 删除联系人delete()
def delete():
    try:
        uid = int(input("请输入要删除的id:"))
        conn.execute("DELETE FROM UserAddrBook WHERE ID=?;", (uid,))
        conn.commit()
        print("删除成功")
    except:
        print("删除失败")


# 根据提示进行各个操作
print("创建个人通讯录表【UserAddrBook】：")
table()
print("查询此表：")
select()
print("增加通讯录用户：")
while 1:
    print("是否需要新增用户？1.是；2.否 (输入所需操作前数字)")
    num = int(input("请输入："))
    if num == 1:
        add()
    else:
        break
print("查询此表：")
select()
print("通过姓名查询此表：")
selectName()
print("删除联系人：")
while 1:
    print("是否需要删除用户？1.是；2.否 (输入所需操作前数字)")
    num = int(input("请输入："))
    if num == 1:
        delete()
    else:
        break
print("查询此表：")
select()
cursor.close()  # 关闭指针对象
conn.close()  # 关闭连接对象
