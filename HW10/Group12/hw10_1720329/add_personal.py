import sqlite3

from personal import personal

conn = sqlite3.connect("personal_communication.db")
list_per = []
per1 = personal('zhangsan', '12347574854', '广东公司', '广东汕头')
list_per.append(per1)
per1 = personal('lisi', '123475755854', '上海公司', '上海浦东')
list_per.append(per1)
for per1 in list_per:
    conn.execute("insert into personal (name, telenumber, companny, address) values('%s', '%s', '%s', '%s')" % (
        per1.name, per1.telenumber, per1.companny, per1.address))
conn.commit()
