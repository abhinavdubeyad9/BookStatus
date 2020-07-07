import sqlite3
Mybooks= sqlite3.connect('Mybooks.db')
curbook=Mybooks.cursor()
curbook.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='books' ''')

#if table doesn't exist
if curbook.fetchone()[0]!=1 :
    curbook.execute('''CREATE TABLE books(
    bookID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author STRING NOT NULL,
    price FLOAT NOT NULL)''')


bID=int(input("enter book ID:"))
bookname=input("enter name of the book:")
bookauth=input("enter name of the author:")
bookprice=float(input("enter price of the book:"))

try:
    curbook.execute("INSERT INTO books(bookID,title,author,price) VALUES(?,?,?,?)", (bID,bookname,bookauth,bookprice))
    Mybooks.commit()
    print("book added successfully")
except:
    print("error in operation.")
    Mybooks.rollback()

Mybooks.close()
