import sqlite3

from person import Person
conn = sqlite3.connect("test.db")
per_name=input('请输入需要查询的名字：')

cur = conn.execute("select * from USER where NAME = '%s'" %(per_name))
r = cur.fetchall()
per_ls = []
for i in r:
    # print (i)
    ID = i[0]
    NAME = i[1]
    TEL = i[2]
    COMPANY = i[3]
    ADDRESS = i[4]
    EMAIL = i[5]
    person = person(ID,NAME,TEL,COMPANY,ADDRESS,EMAIL)
    per_ls.append(person)

for per in per_ls:
    print(per.ID,per.NAME, per.TEL,per.COMPANY,per.ADDRESS,per.EMAIL)