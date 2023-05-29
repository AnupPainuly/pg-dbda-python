

import pymysql

conn=pymysql.connect(host='localhost', port=3306, user='root', 
                                               passwd='root123', db='test')
if conn!=None:
    print("connection done")
else:
    print("connection not done ")
    
def displayall():
    cursor.execute("select * from product")
    for row in cursor.fetchall():
        print(f"Id : {row[0]} Name : {row[1]} Qty : {row[2]} price: {row[3]}")
def addnewproduct():
    pid=int(input("enter pid"))
    pnm=input("enetr name")
    qty=int(input("enter qty"))
    price=float(input("enter price"))
    cursor.execute("insert into product values(%s,%s,%s,%s)",(pid,pnm,qty,price))
    conn.commit()
    
def displaybyId(pid):
    cursor.execute("select * from product where pid=%s",(pid,))
    row=cursor.fetchone()
    print(f"Id : {row[0]} Name : {row[1]} Qty : {row[2]} price: {row[3]}")
    
def updateByid(pid,qty,price):
    try:
        cursor.execute("update product set qty=%s,price=%s where pid=%s",(qty,price,pid))
        conn.commit()
    except:
        conn.rollback()

def deletebyId(pid):
    try:
        cursor.execute("delete from product where pid=%s",(pid,))
        conn.commit()
    except:
        conn.rollback()
    
cursor=conn.cursor();

choice=0

while choice!=6:
    try:
        choice=int(input("""1. add new product
                         2. delete by id
                         3. update by id
                         4. display all
                         5. display by id
                         6. exit
                         choice : """))
        if choice==1:
            addnewproduct()
        elif choice==2:
            pid=int(input("enetr pid"))
            deletebyId(pid)
        elif choice==3:
            pid=int(input("enetr pid"))
            qty=int(input("enetr new qty"))
            price=int(input("enetr new price"))
            updateByid(pid,qty,price)
        elif choice==4:
            displayall()
        elif choice==5:
            pid=int(input("enetr pid"))
            displaybyId(pid)
        elif choice==6:
            print("Thank you for visiting....")
    except ValueError:
        print("pls enter choice")
    