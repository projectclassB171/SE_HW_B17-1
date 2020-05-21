import sqlite3

conn = sqlite3.connect('student_admin.db')

# conn.execute("create table people( ID varchar(10) primary key, name text not null, age text )")
conn.execute('''CREATE TABLE PEOPLE
(NAME TEXT NOT NULL,
PHONE INT PRIMARY KEY NOT NULL,
COMPANY TEXT NOT NULL,
ADDRESS TEXT NOT NULL);''')
conn.commit()

conn.execute("INSERT INTO PEOPLE (NAME,PHONE,COMPANY,ADDRESS) \
      VALUES ('张三',13500022333,'阿斯蒂芬', '意大利')")

conn.commit()

cursor = conn.execute("SELECT NAME, PHONE, COMPANY, ADDRESS from PEOPLE")
for row in cursor:
    print("NAME = ", row[0])
    print("PHONE = ", row[1])
    print("COMPANY = ", row[2])
    print("ADDRESS = ", row[3])

conn.execute("DELETE from PEOPLE where NAME='张三';")

conn.commit()
conn.close()
