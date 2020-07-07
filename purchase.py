import sqlite3
Mybooks= sqlite3.connect('Mybooks.db')
totalprice=0
morebook='Y'

while (morebook=='Y'):
    nm=input("enter the name of the book:")
    sql="SELECT * from books WHERE title='"+nm+"';"
    curbook=Mybooks.cursor()
    curbook.execute(sql)

    record=curbook.fetchone()
    print(record)
    price=record[3]
    copies=float(input("enter no. of copies:"))
    bookprice=price*copies
    totalprice=totalprice+bookprice

    morebook=input("Add more books?Y/N ")
    
print("Total Cost : {}".format(totalprice))
Mybooks.close()



