import sqlite3

conn = sqlite3.connect("address_book.db")

name = input("请输出删除人姓名：")
cur = conn.execute("delete from person where name = '{}';".format(name))
print("删除成功！")

conn.commit()
conn.close()