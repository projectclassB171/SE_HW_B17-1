# 编写一个Python程序，采用SQLite数据库实现通讯录管理功能。
# v采用SQLite数据库存放个人通讯录，要求存放联系人的姓名、电话、公司、地址；
# v设计相应的函数完成以下数据库操作：
# n创建数据库表；
# n新增联系人；
# n按姓名查询联系人详细信息；
# n删除联系人；
import sqlite3

class Phone:
    def __init__(self):
        # 连接数据库
        self.conn = sqlite3.connect('E:\python\\xy\\phone.db')
        print("Opened database successfully")
        print("_____________________________________________")
    # 创建数据库表
    def create_table(self):
        self.conn.execute('''CREATE TABLE 联系人表
            (ID INT PRIMARY KEY     NOT NULL,
            姓名            TEXT    NOT NULL,
            电话       TEXT    NOT NULL,
            公司         TEXT,
            地址         TEXT);''')

    print("联系人表创建成功")
    print("_____________________________________________")
    #插入数据语句
    def insert(self, id='null', name='null', phone='null', company='null', adress='null'):
        self.conn.execute("INSERT INTO 联系人表 (ID,姓名,电话,公司,地址) \
        VALUES('%d', '%s', '%s', '%s', '%s')" % (id, name, phone, company, adress))
        self.conn.commit()
        print("插入成功！")
        print("_____________________________________________")
    # 查询语句
    # 按姓名查询联系人详细信息
    def search_by_name(self, name):
        cursor1 = self.conn.execute("SELECT * from 联系人表 where 姓名 = '%s'" % (name))
        for row in cursor1:
            print("ID = ", row[0])
            print("姓名 = ", row[1])
            print("电话 = ", row[2])
            print("公司 = ", row[3])
            print("地址 = ", row[4])
            print("查询成功！")
            print("_____________________________________________")
    # 删除数据语句
    def delete(self, id):
        self.conn.execute("delete from 联系人表 where ID = '%s'" % (id))
        self.conn.commit()
        print("删除成功")
        print("_____________________________________________")

    # 查询联系表人的所有信息
    def select_all(self):
        cursor2 = self.conn.execute("SELECT * from 联系人表")
        for row in cursor2:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("TELEPHONE = ", row[2])
            print("COMPANY = ", row[3])
            print("ADDRESS = ", row[4])
            print("操作成功")
            print("_____________________________________________")


main = Phone()
main.create_table()
# 插入语句
main.insert(1, 'karry', '1989874678', '88857604', '上海')
main.insert(2, '一一', '17676767564', '98770526', '云南')
main.insert(3, '二二', '15676545654', '89898765', '湖南')
# 从联系人表中查询所有信息
main.select_all()
#从联系人表中查询‘karry’
main.search_by_name('karry')
# 从联系人表中删除id为2的联系人
main.delete(2)

main.select_all()

# 结果：
# Augenstern:
# 联系人表创建成功
# _____________________________________________
# Opened database successfully
# _____________________________________________
# 插入成功！
# _____________________________________________
# 插入成功！
# _____________________________________________
# 插入成功！
# _____________________________________________
# ID =  1
# NAME =  karry
# TELEPHONE =  1989874678
# COMPANY =  88857604
# ADDRESS =  上海
# 操作成功
# _____________________________________________
# ID =  2
# NAME =  一一
# TELEPHONE =  17676767564
# COMPANY =  98770526
# ADDRESS =  云南
# 操作成功
# _____________________________________________
# ID =  3
# NAME =  二二
# TELEPHONE =  15676545654
# COMPANY =  89898765
# ADDRESS =  湖南
# 操作成功
# _____________________________________________
#
# Augenstern:
# ID =  1
# 姓名 =  karry
# 电话 =  1989874678
# 公司 =  88857604
# 地址 =  上海
# 查询成功！
# _____________________________________________
# 删除成功
# _____________________________________________
# ID =  1
# NAME =  karry
# TELEPHONE =  1989874678
# COMPANY =  88857604
# ADDRESS =  上海
# 操作成功
# _____________________________________________
# ID =  3
# NAME =  二二
# TELEPHONE =  15676545654
# COMPANY =  89898765
# ADDRESS =  湖南
# 操作成功
# _____________________________________________
