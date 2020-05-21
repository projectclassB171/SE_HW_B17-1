import sqlite3
conn=sqlite3.connect('E:\wujinchao.db')
print("数据库连接成功!")
cursor = conn.cursor()

try:
    conn.execute('''CREATE TABLE USER
    (id INT PRIMARY KEY NOT NULL,
    name VARCHAR(20) NOT NULL,
    phone CHAR(11) NOT NULL,
    company VARCHAR(50) NOT NULL,
    address VARCHAR(50));''')
    print("Table created successfully")
except:
    print("表已存在!\n")

#添加
try:
    id = int(input('请输入用户ID: '))
    name = str(input('请输入用户名: '))
    phone = str(input('请输入手机号: '))
    company = str(input('请输入用户公司: '))
    address = str(input('请输入用户地址: '))
    sql = "insert into user(id,name,phone,company,address) values(?,?,?,?,?)"
    cursor.execute(sql, (id, name, phone, company, address))
    conn.commit()
    print("保存成功")
    conn.rollback()
except:
    print("保存失败")

#查询
try:
    name = input("请输入查询的用户的姓名")
    cursor.execute("SELECT * From user WHERE name=?;", (name,))
    print("结果为",cursor.fetchone())
except:
    print("输入有误\n")

#删除
try:
    id=int(input('请输入删除信息的id： '))
    conn.execute("delete from user where ID=?;",(id,))
    conn.commit()
    print("删除成功!")
except:
    print("删除失败!")
