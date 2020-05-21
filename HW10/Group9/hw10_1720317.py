import sqlite3

"""
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。 
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址； 
设计相应的函数完成以下数据库操作： 
1、创建数据库表； 
2、新增联系人； 
3、按姓名查询联系人详细信息； 
4、删除联系人；"""


class People:
    def __init__(self, name, phone, company, address):
        self.name = name
        self.phone = phone
        self.company = company
        self.address = address

    def __str__(self):
        return "姓名：{}；联系电话：{}；公司：{}，；地址：{}".format(self.name, self.phone, self.company, self.address)


# 创建表
def conn_db(connect):
    connect.execute(
        "CREATE TABLE DIRECTORIES(ID INTEGER PRIMARY KEY autoincrement,NAME TEXT NOT NULL,PHONE CHAR(11),COMPANY CHAR(50),ADDRESS CHAR(50) )")
    print("创建表成功！\n")
    connect.commit()


# 插入数据
def insertPeople(connect, people2):
    connect.execute("INSERT INTO DIRECTORIES(NAME ,PHONE,COMPANY,ADDRESS) VALUES ('%s','%s','%s','%s')" % (
        people2.name, people2.phone, people2.company, people2.address))
    print("添加数据成功！\n")
    connect.commit()


# 根绝姓名查找
def selectPeopleByName(connect, name1):
    cur = connect.execute("SELECT NAME,PHONE,COMPANY,ADDRESS from DIRECTORIES where NAME='%s'" % name1)
    r = cur.fetchall()
    if len(r) <=0:
        print("没有找到此用户！")
    else:
        people_list = []
        for i in r:
            nameR = i[0]
            phoneR = i[1]
            companyR = i[2]
            addressR = i[3]
            peopleResult = People(nameR, phoneR, companyR, addressR)
            people_list.append(peopleResult)
        print("查询结果：")
        for peopleQuery in people_list:
            print(peopleQuery)
            print()
    cur.close()


# 根据ID删除
def delPeopleByID(connect, peopleID):
    result = connect.execute("DELETE from DIRECTORIES where ID='%d'" % peopleID)
    print(result.rowcount)
    if result.rowcount == 0:
        print("删除失败，没有找到此用户！")
    else:
        print('删除成功！')
    result.close()
    connect.commit()


conn = sqlite3.connect("addressBook.db")  # 连接 数据库
conn_db(conn)  # 创建表
operate = 1
while operate != 0:
    operate = int(input("请选择操作：0退出，1新增用户，2按姓名查询联系人详细信息，3根据ID删除联系人"))
    if operate == 0:
        conn.close()
        break
    elif operate == 1:
        name = input("请输入姓名：")
        phone = input("请输入电话：")
        company = input("请输入公司：")
        address = input("请输入地址：")
        people = People(name, phone, company, address)
        insertPeople(conn, people)
        continue
    elif operate == 2:
        name = input("请输入要查找的联系人姓名：")
        selectPeopleByName(conn, name)  # 根据姓名查找
        continue
    elif operate == 3:
        ID = int(input("请输入要删除的联系人的ID："))
        delPeopleByID(conn, ID)  # 根据ID删除
        continue
    else:
        print("操作有误，自动退出程序！")
        conn.close()
        break
