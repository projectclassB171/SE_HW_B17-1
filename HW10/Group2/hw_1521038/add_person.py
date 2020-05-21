import sqlite3

from 通讯录管理.person import Person

conn = sqlite3.connect("address_book.db")
name = input("请输出姓名：")
tel = input("请输出电话：")
company = input("请输出公司：")
addr = input("请输出地址：")
list_per = []
per1 = Person(name, tel, company, addr)
list_per.append(per1)
for per1 in list_per:
    conn.execute("insert into person(name, tel, company, addr) values('%s', '%s', '%s', '%s')" % (per1.name, per1.tel, per1.company, per1.addr))
print("增加联系人成功！")
conn.commit()