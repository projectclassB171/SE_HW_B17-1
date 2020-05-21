"""
编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
创建数据库表；
新增联系人；
按姓名查询联系人详细信息；
删除联系人；
"""



import sqlite3
conn = sqlite3.connect('address_book.db')
cur = conn.cursor()
#创建数据库表
cur.execute("CREATE TABLE address "
            "(id INT PRIMARY KEY, "
            "name  text    NOT NULL, "
            "phone     CHAR(11), "
            "company   CHAR(50), "
            "addr      CHAR(50))")
conn.commit()

#添加联系人
cur.execute("insert into address (id, name, phone, company, addr) values (1, 'zz', '12472583652', 'A', '北京')")
cur.execute("insert into address (id, name, phone, company, addr) values (2, 'xx', '12345678911', 'S', '上海')")
cur.execute("insert into address (id, name, phone, company, addr) values (3, 'cc', '12578585575', 'D', '广东')")
cur.execute("insert into address (id, name, phone, company, addr) values (4, 'vv', '12655477524', 'F', '深圳')")
conn.commit()

sele = cur.execute("select name, phone, company, addr from address ")
res = sele.fetchall()
for i in res:
    print("姓名:{}".format(i[0]))
    print("联系电话:{}".format(i[1]))
    print("公司:{}".format(i[2]))
    print("地址:{}".format(i[3]))

#查询联系人
s = input("请输入你要查询的联系人姓名：")
sele = cur.execute("select name, phone, company, addr from address where name like '%" + s + "%'")
res = sele.fetchall()
if len(res) == 0:
    print("该联系人不存在")
else:
    for i in res:
        print("姓名:{}".format(i[0]))
        print("联系电话:{}".format(i[1]))
        print("公司:{}".format(i[2]))
        print("地址:{}".format(i[3]))



#删除联系人
d = input("请输入所要删除的联系人姓名:")
cursor = cur.execute("SELECT name from address where name = '%s';" % d)
for row in cursor:
    if d == row[0]:
        cur.execute("DELETE from address where name ='%s';" % d)
        conn.commit()
        print("成功删除联系人信息！！")
        break
    else:
        print("该联系人不存在！！")

sele = cur.execute("select name, phone, company, addr from address ")
res = sele.fetchall()
for i in res:
    print("姓名:{}".format(i[0]))
    print("联系电话:{}".format(i[1]))
    print("公司:{}".format(i[2]))
    print("地址:{}".format(i[3]))
conn.close()


"""
E:\5.20\venv\Scripts\python.exe E:/5.20/hw10_1720305.py
姓名:zz
联系电话:12472583652
公司:A
地址:北京
姓名:xx
联系电话:12345678911
公司:S
地址:上海
姓名:cc
联系电话:12578585575
公司:D
地址:广东
姓名:vv
联系电话:12655477524
公司:F
地址:深圳
请输入你要查询的联系人姓名：zz
姓名:zz
联系电话:12472583652
公司:A
地址:北京
请输入所要删除的联系人姓名:zz
成功删除联系人信息！！
姓名:xx
联系电话:12345678911
公司:S
地址:上海
姓名:cc
联系电话:12578585575
公司:D
地址:广东
姓名:vv
联系电话:12655477524
公司:F
地址:深圳

Process finished with exit code 0

"""

