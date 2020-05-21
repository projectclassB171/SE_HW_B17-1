import sqlite3
conn = sqlite3.connect("address_book.db")
conn.execute("create table person( ID varchar(10) primary key, name text not null, tel varchar(11), company text, "
             "addr text not null)")
conn.commit()