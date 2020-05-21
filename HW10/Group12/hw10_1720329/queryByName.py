import sqlite3

conn = sqlite3.connect("personal_communication.db")
c = conn.cursor()

i = input("请输入所要查找的联系人姓名:")
sql1 = "SELECT name,telenumber,companny, address from personal where name like '%" + i + "%'"
cursor = c.execute(sql1)
res = cursor.fetchall()
if len(res) == 0:
    print("该联系人不存在！！")
else:
    for row in res:
        print("姓名:{0}".format(row[0]))
        print("电话号码:{0}".format(row[1]))
        print("公司:{0}".format(row[2]))
        print("地址:{0}".format(row[3]))
