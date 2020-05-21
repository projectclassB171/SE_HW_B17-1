import sqlite3
import os

def CreateDataBase():
    con = sqlite3.connect('1720309.db')
    cur = con.cursor()
    stable = """
	create table contract
	(
		id int(10) primary key,
		name varchar(20) not null,
		telp char(11) not null,
		com char(15),
		addr varchar(50)
	)
	"""
    cur.execute(stable)
    cur.close()
    con.close()


def Insert(con, cur):
    id = int(input('请输入id: '))#输入需要插入的工号id
    name = str(input('请输入name: '))#输入需要插入的名字name
    telp = str(input('请输入telp: '))#输入需要插入的手机号码telp
    com = str(input('请输入com: '))#输入需要插入的公司名称com
    addr = str(input('请输入addr: '))#输入需要插入的地址addr
    sql = "insert into contract(id,name,telp,com,addr) values(?,?,?,?,?)"
    try:
        cur.execute(sql, (id, name, telp, com, addr))
        con.commit()
    except:
        con.rollback()


def Delete(con, cur):
    SelectInfo(con, cur)
    did = int(input('请输入要删除的id号: '))
    sql = "delete from contract where id=?"
    try:
        cur.execute(sql, (did,))
        con.commit()
    except:
        con.rollback()


def Update(con, cur):
    SelectInfo(con, cur)
    did = int(input('请输入需要更新的id号: '))
    sqlname = "update contract set name=? where id=?"
    name = str(input('请输入名字name: '))
    try:
        cur.execute(sqlname, (name, did))
        con.commit()
    except:
        con.rollback()

    sqltelp = "update contract set telf=? where id=?"
    telp = str(input('请输入手机号telp: '))
    try:
        cur.execute(sqltelp, (telp, did))
        con.commit()
    except:
        con.rollback()

    sqlcom = "update contract set tels=? where id=?"
    com = str(input('请输入公司名称com: '))
    try:
        cur.execute(sqlcom, (com, did))
        con.commit()
    except:
        con.rollback()

    sqladdr = "update contract set other=? where id=?"
    other = str(input('请输入地址add: '))
    try:
        cur.execute(sqladdr, (other, did))
        con.commit()
    except:
        con.rollback()


def SelectInfo(con, cur):
    cur.execute("select * from contract")
    result = cur.fetchall()
    print(result)


def Meau():
    print('1.显示所有信息')
    print('2.插入个人信息')
    print('3.更新个人信息')
    print('4.删除个人信息')
    print('0.退出')
    sel = 9
    while (sel > 5 or sel < 0):
        sel = int(input('请输入相应的数字进行操作: '))
    return sel


def main():
    if os.path.exists('1720309.db') == False:
        CreateDataBase()
    con = sqlite3.connect('1720309.db')
    cur = con.cursor()
    while (True):
        sel = Meau()
        if (sel == 1):
            SelectInfo(con, cur)
        elif (sel == 2):
            Insert(con, cur)
        elif (sel == 3):
            Update(con, cur)
        elif (sel == 4):
            Delete(con, cur)
        else:
            break
        print('-------------------------')
    cur.close()
    con.close()


if __name__ == "__main__":
    main()


