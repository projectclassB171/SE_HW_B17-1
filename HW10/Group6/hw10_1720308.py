1、编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
设计相应的函数完成以下数据库操作：
创建数据库表；
新增联系人；
按姓名查询联系人详细信息；
删除联系人：

mport sqlite3
conn = sqlite3.connect('1720308.db')
print("Opened database successfully.")
c = conn.cursor()
#创建数据库表
cur.execute("CREATE TABLE user "
            "(id INT PRIMARY KEY, "
            "name  text    NOT NULL, "
            "phone     CHAR(11), "
            "company   CHAR(50), "
            "addr      CHAR(50))")
conn.commit()

#添加联系人
def insert():
    ID = input('请输入联系人id号:\n')
    NAME = raw_input('请输入联系人名称:\n')
    PHONE = input('请输入手机号码:\n')
    COMPANY = raw_input('请输入联系人公司:\n')
    ADDRESS = input('请输入联系人地址:\n')
    sql1 = 'insert into USER(ID,NAME,PHONE,COMPANY,ADDRESS)'
    sql1 += 'values("%s","%s","%s","%s","%s");' % (ID, NAME, PHONE, COMPANY, ADDRESS)
    conn.execute(sql1)
    conn.commit()
    print("添加成功！")

#查询联系人
conn = sqlite3.connect('people.db')


def query():
    conn = sqlite3.connect('people.db')
    name = raw_input('请输入要查询的联系人姓名：')
    sql2 = "SELECT ID,NAME,PHONE,COMPANY,ADDRESS from USER where name= '%s';" % (name)
    cursor = conn.execute(sql2)
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("PHONE = ", row[2])
        print("COMPANY = ", row[3])
        print("ADDRESS = ", row[4], "\n")
        break
    else:
        print("输入错误!没有该联系人！")


#删除联系人
d = input("请输入所要删除的联系人姓名:")
cursor = cur.execute("SELECT name from user where name = '%s';" % d)
for row in cursor:
    if d == row[0]:
        cur.execute("DELETE from user where name ='%s';" % d)
        conn.commit()
        print("成功删除联系人信息！！")
        break
    else:
        print("该联系人不存在！！")

sele = cur.execute("select id, name, phone, company，address from user ")
res = sele.fetchall()
for i in res:
    print("id:{}".format(i[0]))
    print("姓名:{}".format(i[0]))
    print("联系电话:{}".format(i[1]))
    print("公司:{}".format(i[2]))
    print("地址:{}".format(i[3]))
conn.close()
# 菜单列表选项
def menu():
    print('1.新增联系人')
    print('2.查询联系人')
    print('3.删除联系人')
    print('4.修改联系人')
    print('5.显示所有联系人')


while True:
    menu()
    x = raw_input('请输入您想要操作前的编号:')
    if x == '1':
        insert()
        continue
    if x == '2':
        query()
        continue
    if x == '3':
        delete()
        continue
    if x == '4':
        change()
        continue
    if x == '5':
        showall()
        continue
    else:
        print("输入错误，请重新输入！")
        continue

