import sqlite3

# conn = sqlite3.connect('addressBook.db')
# print("数据库已连接！")
# c = conn.cursor()
# c.execute('''
# CREATE TABLE person_Msg
#    (NAME           TEXT    NOT NULL,
#    TEL            INT     NOT NULL,
#    COMPANY        TEXT    NOT NULL,
#    ADDRESS        CHAR(50));
# ''')
# print("通讯录表已创建")
# conn.commit()
# conn.close()


newname = input("请输入新建联系人姓名：")
newtel = input("请输入新建联系人电话号码：")
newcompany = input("请输入新建联系人公司名称：")
newaddr = input("请输入新建联系人住址：")
ob = (newname, newtel, newcompany, newaddr)
conn = sqlite3.connect('addressBook.db')
c = conn.cursor()
c.execute("INSERT INTO person_Msg (NAME,TEL,COMPANY,ADDRESS) \
   VALUES (?,?,?,?)",ob)
conn.commit()
print("添加成功！")
conn.close()
print()


print("查询联系人")
sname = input("请输入联系人姓名：")
conn = sqlite3.connect('addressBook.db')
c = conn.cursor()
c.execute("SELECT name,tel,company,address from person_Msg WHERE name = ?;",(sname,))
print(c.fetchall())
print("查询成功")
conn.close()

print("删除联系人")
dname = input("请输入联系人姓名：")
conn = sqlite3.connect('addressBook.db')
c = conn.cursor()
c.execute("DELETE from person_Msg WHERE name = ?;",(dname,))
conn.commit()
print("删除成功")
conn.close()



