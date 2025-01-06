from tkinter import *
import mysql.connector
import pandas as pd
import numpy as np

mydb=mysql.connector.connect(host="localhost",user="admin",passwd="admin",database="driverhire")
mycur=mydb.cursor()
win = Tk()

def addrec():
        drid=t1.get()
        sql="select * from customers where custcode='" + drid +"'"
        mycur.execute(sql)
        res=mycur.fetchone()
        if res:
            l18.configure(text= "Customer Code Already Found")
            
        else:
            sql="insert into customers values('" + drid + "','" + t2.get() + "','" + t3.get() +"','"+ t4.get() +"','" + t5.get() + "','" + t6.get() + "','" + t7.get() + "','" + t8.get() +"','"+ t9.get() +"','" + t10.get() + "','" + t11.get() + "')"
            mycur.execute(sql)
            mydb.commit()
            l18.configure(text= "Customer Profile Added")
def viewrec():
        drid=t1.get()
        sql="select * from customers where custcode='" + drid +"'"
        mycur.execute(sql)
        res=mycur.fetchone()
        if res:
            t2.insert(END, res[1])
            t3.insert(END, res[2])
            t4.insert(END, res[3])
            t5.insert(END, res[4])
            t6.insert(END, res[5])
            t7.insert(END, res[6])
            t8.insert(END, res[7])
            t9.insert(END, res[8])
            t10.insert(END, res[9])
            t11.insert(END, res[10])
          
            
        else:
            l18.configure(text= "Customer Code Missing")
def reportrec():
        fyear=t1.get()
        sql="select * from customers"
        mycur.execute(sql)
        res=mycur.fetchall()
        if res:
            print()
            print()
            print()
            print()
            print()
            print()
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("                                 Customer Details and Status Report")
            print("------------------------------------------------------------------------------------------------------------------------------")
            #print("Code  Customer Name   Gender Street      Area    City   Since    Location   Mobile No  Alternate No   Status")
            #print("------------------------------------------------------------------------------------------------------------------------------")
            #for rec in res:
                  #print( rec[0], rec[1],  rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8],rec[9],rec[10])
                  #c1=rec[0]
                  #c2=rec[1]
                  #c3=rec[2]
                  #c4=rec[3]
                  #c5=rec[4]
                  #c6=rec[5]
                  #c7=rec[6]
                  #c8=rec[7]
                  #c9=rec[8]
                  #c10=rec[9]
                  #c11=rec[10]  
                  #print('%10s %8s %7s %8s %10s %20s %20s %10s %20s %20s'%( str(rec[0]), str(rec[1]),str(rec[2]),str(rec[3]),str(rec[4]),str(rec[5]),str(rec[6]),str(rec[7]),str(rec[8]),str(rec[9]),str(rec[10])))
                  #print('%10s %8s %7s %8s %10s %20s %20s %10s %20s %20s'%( str(c1), str(c2),str(c3),str(c4),str(c5),str(c6),str(c7),str(c8),str(c9),str(c10),str(c11)))
            sqlst=pd.read_sql("select * from customers",mydb)
            #pd.set_option('display.max_columns', 11)
            pd.set_option('display.max_columns', 11)
            pd.set_option('display.width', 200)
            df = pd.DataFrame(sqlst,columns=['Custcode','Custname','Gender','Street','Location','City','Customersince','Landmark','Phoneno','Alternateno','Status'])
            #df = pd.DataFrame(sqlst,columns=['custcode','custname','gender','street','location','city','phoneno','alternateno','status'])        
            #print(df)
            for n in list(df.columns):
                    print (n, end="    ")
            print()
            print("------------------------------------------------------------------------------------------------------------------------------")
            for row in df.values:
                    for data in row:
                            print(data, end="   ")
                    print()
                    print("------------------------------------------------------------------------------------------------------------------------------")
           
            print("                                 End of Report")
            print("------------------------------------------------------------------------------------------------------------------------------")
               
           
           
        else:
            l18.configure(text= "Customer details Missing")
            
def deleterec():
        drid=t1.get()
        sql="select * from customers where custcode='" + drid +"'"
        mycur.execute(sql)
        res=mycur.fetchone()
        if res:
            sql="delete from customers where custcode='" + drid +"'"
            mycur.execute(sql)
            mydb.commit()
            l18.configure(text= "Customer details deleted")
        else:
            l18.configure(text= "Customer Code Missing")
def clearall():
    l18.configure(text= "")
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)
    t5.delete(0,END)
    t6.delete(0,END)
    t7.delete(0,END)
    t8.delete(0,END)
    t9.delete(0,END)
    t10.delete(0,END)
    t11.delete(0,END)
    
def close():
    win.destroy()
                      
l1 = Label(win,text="Driver Hiring System ")
l1.grid(column=1,row=0)

lmsg = Label(win,text="NS Drivers Desk - Pollachi ")
lmsg.grid(column=3,row=0)

l2 = Label(win,text=" Customer Details Maintenance")
l2.grid(column=1,row=1)

l3 = Label(win,text="Customer Code")
l3.grid(column=0,row=2,ipady=10)

l4 = Label(win,text="Customer Name ")
l4.grid(column=0,row=3,ipady=10)

l5 = Label(win,text="Gender [M/F] ")
l5.grid(column=0,row=4,ipady=10)

l6 = Label(win,text="Street ")
l6.grid(column=0,row=5,ipady=10)

l7 = Label(win,text="Location  ")
l7.grid(column=0,row=6,ipady=10)

l8 = Label(win,text="City")
l8.grid(column=0,row=7,ipady=10)

l9 = Label(win,text="Customer Since")
l9.grid(column=0,row=8,ipady=10)

l10 = Label(win,text="Landmark ")
l10.grid(column=0,row=9,ipady=10)


l11 = Label(win,text="Phone no ")
l11.grid(column=0,row=10,ipady=10)


l12 = Label(win,text="Alternate No. ")
l12.grid(column=0,row=11,ipady=10)


l13 = Label(win,text="Customer Status")
l13.grid(column=0,row=12,ipady=10)



l18 = Label(win,)
l18.grid(column=5,row=10)





t1 = Entry(win)
t1.grid(column=1,row=2,ipadx=10)

t2 = Entry(win)
t2.grid(column=1,row=3,ipadx=10)

t3 = Entry(win)
t3.grid(column=1,row=4,ipadx=10)

t4 = Entry(win)
t4.grid(column=1,row=5,ipadx=10)

t5 = Entry(win)
t5.grid(column=1,row=6,ipadx=10)

t6 = Entry(win)
t6.grid(column=1,row=7,ipadx=10)

t7 = Entry(win)
t7.grid(column=1,row=8,ipadx=10)

t8 = Entry(win)
t8.grid(column=1,row=9,ipadx=10)

t9 = Entry(win)
t9.grid(column=1,row=10,ipadx=10)

t10 = Entry(win)
t10.grid(column=1,row=11,ipadx=10)

t11 = Entry(win)
t11.grid(column=1,row=12,ipadx=10)





b1 = Button(win,text=" Add ", command=addrec)
b1.grid(column=3,row=10,ipadx=20)

b2 = Button(win,text=" View ", command=viewrec)
b2.grid(column=4,row=10,ipadx=20)

b3= Button(win,text='Delete',command=deleterec)
b3.grid(column=3,row=11,ipadx=20)

b4 = Button(win,text='Report',command=reportrec)
b4.grid(column=4,row=11,ipadx=20)

b5 = Button(win,text='Clear',command=clearall)
b5.grid(column=3,row=12,ipadx=20)

b6 = Button(win,text='Exit',command=close)
b6.grid(column=4,row=12,ipadx=20)





#win.configure(bg="blue")

win.geometry("600x700")
win.mainloop()
