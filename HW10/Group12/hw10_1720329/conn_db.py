import sqlite3

conn = sqlite3.connect('personal_communication.db')
conn.execute("create table personal"
             "( ID varchar(10) primary key,"
             " name text not null,"
             "telenumber text,"
             " companny char(50),"
             "address char(50))")
conn.commit()
