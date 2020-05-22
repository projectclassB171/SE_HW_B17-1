import sqlite3

from hw10_1720327.person_admin.person import Person

conn = sqlite3.connect("person_admin.db")
list_per = []
per1 = Person('zhaosi', '15165451', 'xxx公司', 'xxx省xxx市xxx区xxx路xxx号')
list_per.append(per1)
per1 = Person('liu', '15646466', 'yyy公司', 'yyy省yyy市yyy区yyy路yyy号')
list_per.append(per1)
for per1 in list_per:
    conn.execute("insert into person (name, phone, company, address) values('%s', '%s', '%s', '%s')" % (per1.name, per1.phone, per1.company, per1.address))
conn.commit()
