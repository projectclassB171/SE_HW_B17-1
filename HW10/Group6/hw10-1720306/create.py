import sqlite3
conn = sqlite3.connect('D:\\hw10-1720306\\test.db')
print("Opened database successfully");
conn.execute('''CREATE TABLE USER11
     (ID INT PRIMARY KEY     NOT NULL,
      
      NAME           TEXT    NOT NULL,
      TEL            TEXT    NOT NULL,
      ADDRESS        TEXT    NOT NULL,
      COMPANY        TEXT    NOT NULL,
      EMAIL          CHAR(50)         );
      ''')
print("Table USER created successfully");

conn.execute('''CREATE TABLE GOODSTYPE 
    (ID INT PRIMARY KEY     NOT NULL, 
     TYPEID         TEXT    NOT NULL, 
     DESCRIPTION    TEXT     NOT NULL); 
      ''')
print("Table GOODSTYPE created successfully");
conn.close()