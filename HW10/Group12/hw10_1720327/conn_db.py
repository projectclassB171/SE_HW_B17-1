import sqlite3
conn = sqlite3.connect('person_admin.db')
conn.execute("create table person( ID varchar(10) primary key, name text not null, phone text, company text, address text )")
conn.commit()

