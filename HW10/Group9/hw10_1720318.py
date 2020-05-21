# coding=utf-8
import _sqlite3

conn = _sqlite3.connect('book.db')
print '连接成功'
cursor = conn.cursor()

conn.execute('''CREATE TABLE USER
    (ID INT PRIMARY KEY     NOT NULL,
    NAME           TEXT    NOT NULL,
    PHONE       TEXT     NOT NULL,
    COMPANY      CHAR(50),
    ADDRESS         CHAR(50));''')
print '创表成功'
conn.close()


def insert():
    _ID = input('请输入联系人id号:\n')
    _NAME = input('请输入联系人名称:\n')
    _PHONE = input('请输入手机号码:\n')
    _COMPANY = input('请输入联系人公司:\n')
    _ADDRESS = input('请输入联系人地址:\n')
    sql1 = 'insert into USER(ID,NAME,PHONE,COMPANY,ADDRESS)'
    sql1 += 'values("%s","%s","%s","%s","%s");' % (_ID, _NAME, _PHONE, _COMPANY, _ADDRESS)
    conn.execute(sql1)
    conn.commit()
    print("添加成功！")


def query():
    conn = _sqlite3.connect('Book.db')
    name = input('请输入要查询的联系人姓名：')
    sql2 = "SELECT ID,NAME,PHONE,COMPANY,ADDRESS from USER where name= '%s';" % (name)
    cursor = conn.execute(sql2)
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("PHONE = ", row[2])
        print("COMPANY = ", row[3])
        print("ADDRESS = ", row[4], "\n")
        break
    else:
        print("输入错误!没有该联系人！")


def delete():
    name = input("请输入所要删除的联系人姓名:")
    cursor = conn.execute("SELECT name from USER where name = '%s';" % name)
    for row in cursor:
        if name == row[0]:
            conn.execute("DELETE from USER where name = '%s';" % name)
            conn.commit()
            print("删除联系人成功！")
            break
    else:
        print("输入错误!没有该联系人！")


def showall():
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


def menu():
    print('1.新增联系人')
    print('2.查询联系人')
    print('3.删除联系人')
    print('4.显示所有联系人')


while True:
    menu()
    x = input('请输入您想要操作前的编号:')
    if x == 1:
        insert()
        continue
    if x == 2:
        query()
        continue
    if x == 3:
        delete()
        continue
    if x == 4:
        showall()
        continue
    else:
        print("输入错误，请重新输入！")
        continue
