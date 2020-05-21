import sqlite3

conn = sqlite3.connect("personal_communication.db")
c = conn.cursor()
i = input("请输入所要删除的联系人姓名:")
cursor = c.execute("SELECT name from personal where name = '%s';" % i)
for row in cursor:
    if i == row[0]:
        c.execute("DELETE from personal where name ='%s';" % i)
        conn.commit()
        print("成功删除联系人信息！！")
        break
    else:
        print("该联系人不存在！！")
