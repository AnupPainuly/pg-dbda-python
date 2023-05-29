# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:09:44 2023

@author: anilk
"""

def displayall():
    cursor.execute("select * from product")
    for row in cursor.fetchall():
        print(f"Id :{row[0]} Name:{row[1]} Quantity : {row[2]} Price: {row[3]}")
        
def addnewProduct():
    pid=int(input("enetr pid"))
    pname=input("enter pname")
    qty=int(input("enetr quantity"))
    price=float(input("enetr price"))
    cursor.execute("insert into product values(?,?,?,?)",(pid,pname,qty,price))
    conn.commit()
    
def deletebyID(pid):
    cursor.execute("delete from product where pid=?",(pid,))
    conn.commit()

def updatebyID(pid,qty,price):    
    cursor.execute("update product set qty=?,price=? where pid=?",(qty,price,pid))
    conn.commit()

def displayById(pid):
    cursor.execute("select * from product where pid=?",(pid,))
    row=cursor.fetchone();
    print(f"Id :{row[0]} Name:{row[1]} Quantity : {row[2]} Price: {row[3]}")
        
import sqlite3
conn=sqlite3.connect(r"mydb.db");
if conn!=None:
    print("connection done")
else:
    print("connection not done")
    
#to create buffer to hold the data
cursor=conn.cursor();

choice=0
while choice!=6:
    choice=int(input("""1. add new product
                     2. delete the product
                     3. update product
                     4. display all
                     5. display by id
                     6. exit"""))
    if choice==1:
        addnewProduct()
    elif choice==2:
        pid=int(input("enter pid to delete"))
        deletebyID(pid)
    elif choice==3:
        pid=int(input("enter pid to update"))
        qty=int(input("enter new qty"))
        price=int(input("enter new price"))
        updatebyID(pid,qty,price)
    elif choice==4:
        displayall()
    elif choice==5:
        pid=int(input("enter pid "))
        displayById(pid)
    elif choice==6:
        print("thank you for visiting.....")
    else:
        print("wrong choice")
