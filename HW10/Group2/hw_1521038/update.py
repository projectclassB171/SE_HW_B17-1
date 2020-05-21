import sqlite3

conn = sqlite3.connect("address_book.db")

name = input("请输入更新联系人的姓名：")
what = input("请输入更新项：")
how = input("请输入更新内容：")

cur = conn.execute("update person set {} = '{}' where name = '{}';".format(what, how, name))
print("更新成功！")

conn.commit()
conn.close()