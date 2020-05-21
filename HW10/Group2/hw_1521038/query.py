import sqlite3

from 通讯录管理.person import Person

conn = sqlite3.connect("address_book.db")

per_name = input("请输入查询人姓名：")
cur = conn.execute("select * from person where name = '{}'".format(per_name))

p = cur.fetchall()
per_ls = []
for i in p:
    name = i[1]
    tel = i[2]
    company = i[3]
    addr = i[4]
    person = Person(name, tel, company, addr)
    per_ls.append(person)

for per in per_ls:
    print("查询结果：")
    print("Name:", per.name)
    print("电话：", per.tel)
    print("公司：", per.company)
    print("地址", per.addr)