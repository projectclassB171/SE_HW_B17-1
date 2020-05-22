import sqlite3
from hw10_1720327.person_admin.person import Person

conn = sqlite3.connect("person_admin.db")

cur = conn.execute("select * from person")

# s =cur.fetchone()
# # print( s, type(s))
# # s =cur.fetchone()
# # print( s, type(s))
#----------------
r = cur.fetchall()
per_ls = []
for i in r:
    # print (i)
    name = i[1]
    phone = i[2]
    company = i[3]
    address = i[4]
    person = Person(name, phone, company, address)
    per_ls.append(person)

for per in per_ls:
    print(per.name,per.phone,per.company,per.address)



