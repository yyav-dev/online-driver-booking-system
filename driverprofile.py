from tkinter import *
import mysql.connector
import pandas as pd
import numpy as np

mydb=mysql.connector.connect(host="localhost",user="admin",passwd="admin",database="driverhire")
mycur=mydb.cursor()
win = Tk()

def addrec():
        drid=t1.get()
        sql="select * from actingdriver where driverid='" + drid +"'"
        mycur.execute(sql)
        res=mycur.fetchone()
        if res:
            l18.configure(text= "Driver ID Already Found")
            
        else:
            sql="insert into actingdriver values('" + drid + "','" + t2.get() + "','" + t3.get() +"','"+ t4.get() +"','" + t5.get() + "','" + t6.get() + "','" + t7.get() + "','" + t8.get() +"','"+ t9.get() +"','" + t10.get() + "','" + t11.get() +  "','" + t12.get() + "','" + t13.get() +"','"+ t14.get() +"','" + t15.get() + "')"
            mycur.execute(sql)
            mydb.commit()
            l18.configure(text= "Driver Profile Added")
def viewrec():
        drid=t1.get()
        sql="select * from actingdriver where driverid='" + drid +"'"
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
            t12.insert(END, res[11])
            t13.insert(END, res[12])
            t14.insert(END, res[13])
            t15.insert(END, res[14])
            
        else:
            l18.configure(text= "Driver ID Missing")
def reportrec():
        fyear=t1.get()
        sql="select * from actingdriver"
        mycur.execute(sql)
        res=mycur.fetchall()
        if res:
            print("------------------------------------------------------------------------------------------------------------------------------")
            print("               Acting Driver Details and Status Report")
            print("------------------------------------------------------------------------------------------------------------------------------")
            sqlst=pd.read_sql("select * from actingdriver",mydb)
            #pd.set_option('display.max_columns', 11)
            pd.set_option('display.max_columns', 15)
            pd.set_option('display.width', 200)
            df = pd.DataFrame(sqlst,columns=['Driverid','Name','Gender','DOB','Licenseno','Validity','Renewal','Street','Location','City','Phoneno','Adharno','Driversince','Driverstatus','Vehicleinfo'])
            for n in list(df.columns):
                    print (n, end="         ")
            print()
            print("------------------------------------------------------------------------------------------------------------------------------")
            #df = pd.DataFrame(sqlst,columns=['driverid','name','gender','licenseno','street','city','phoneno','aadharno','driverstatus','vehicleinfo'])        
            #print(df)
            for row in df.values:
                    for data in row:
                            print(data, end="   ")
                    print()
                    print("------------------------------------------------------------------------------------------------------------------------------")
           
            print("                                 End of Report")
            print("------------------------------------------------------------------------------------------------------------------------------")
                       
           
            
        else:
            l18.configure(text= "Driver details Missing")
            
def deleterec():
        drid=t1.get()
        sql="select * from actingdriver where driverid='" + drid +"'"
        mycur.execute(sql)
        res=mycur.fetchone()
        if res:
            sql="delete from actingdriver where driverid='" + drid +"'"
            mycur.execute(sql)
            mydb.commit()
            l18.configure(text= "Acting Driver details deleted")
        else:
            l18.configure(text= "Acting Driver ID Missing")
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
    t12.delete(0,END)
    t13.delete(0,END)
    t14.delete(0,END)
    t15.delete(0,END)
    
def close():
    win.destroy()
                      
l1 = Label(win,text="Driver Hiring System ")
l1.grid(column=1,row=0)

l2 = Label(win,text=" Driver Details Maintenance")
l2.grid(column=1,row=1)
lmsg = Label(win,text="NS Drivers Desk - Pollachi ")
lmsg.grid(column=3,row=0)
l3 = Label(win,text="Driver Code")
l3.grid(column=0,row=2,ipady=10)

l4 = Label(win,text="Driver Name ")
l4.grid(column=0,row=3,ipady=10)

l5 = Label(win,text="Gender [M/F] ")
l5.grid(column=0,row=4,ipady=10)

l6 = Label(win,text="Birth Date ")
l6.grid(column=0,row=5,ipady=10)

l7 = Label(win,text="License No.  ")
l7.grid(column=0,row=6,ipady=10)

l8 = Label(win,text="License Validity")
l8.grid(column=0,row=7,ipady=10)

l9 = Label(win,text="Next Renewal")
l9.grid(column=0,row=8,ipady=10)

l10 = Label(win,text="Steet ")
l10.grid(column=0,row=9,ipady=10)


l11 = Label(win,text="Location ")
l11.grid(column=0,row=10,ipady=10)


l12 = Label(win,text="City ")
l12.grid(column=0,row=11,ipady=10)


l13 = Label(win,text="Phone No. ")
l13.grid(column=0,row=12,ipady=10)


l14 = Label(win,text="Aadhar No. ")
l14.grid(column=0,row=13,ipady=10)


l15 = Label(win,text="Driver Since ")
l15.grid(column=0,row=14,ipady=10)


l16 = Label(win,text="Driver Status ")
l16.grid(column=0,row=15,ipady=10)


l17 = Label(win,text="Vehicle Type ")
l17.grid(column=0,row=16,ipady=10)



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

t12 = Entry(win)
t12.grid(column=1,row=13,ipadx=10)

t13 = Entry(win)
t13.grid(column=1,row=14,ipadx=10)

t14 = Entry(win)
t14.grid(column=1,row=15,ipadx=10)

t15 = Entry(win)
t15.grid(column=1,row=16,ipadx=10)



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

win.geometry("600x800")
win.mainloop()
