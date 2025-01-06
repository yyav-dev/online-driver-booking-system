import sys
import os
from tkinter import *
import mysql.connector
from datetime import date


mydb=mysql.connector.connect(host="localhost",user="admin",passwd="admin",database="driverhire")
mycur=mydb.cursor()

class MyWindow:
    def __init__(self, win):
        self.lbl10=Label(win, text='NS Drivers Desk, Pollachi')
        self.lbl1=Label(win, text='Driver Hiring System')
        self.lbl5=Label(win, text='Admin Login Entry')
        
        self.lbl2=Label(win, text='User Name')
        self.lbl3=Label(win, text='Password')
        self.lbl4=Label(win)

        self.t1=Entry()
        self.t2=Entry( show='*')
        ds='Date : ' + str(date.today())
        self.b1 = Button(win, text='Login',command=self.logcode)
        self.b2=Button(win, text='Reset', command=self.clearcode)
        self.b3 = Button(win, text='Close', command=self.closecode)
        self.b4 = Label(win, text=ds)

        self.lbl5.place(x=100, y=50)
        self.lbl1.place(x=100, y=30)
        self.lbl10.place(x=100,y=10)
        self.t1.place(x=200, y=100) 
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=150)
        self.lbl3.place(x=100, y=150)
        
        self.lbl4.place(x=100, y=225)
        
        
       
        self.b1.place(x=100, y=200)
        self.b2.place(x=175, y=200)
        self.b3.place(x=250, y=200)
        self.b4.place(x=150, y=250)
       
     
    def logcode(self):
         sql = "select * from adminlogin where adminid='"+self.t1.get()+"' and adminpass='"+self.t2.get()+"'"
         mycur.execute(sql)
         res=mycur.fetchall()
         if res:
             os.system('python drivermenu.py')
         else:
             self.lbl4.configure(text="Login Failed. Check Name / Password")
             
    def clearcode(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.lbl4.configure(text="")
    def closecode(self):
        window.destroy()
    
            
window=Tk()
mywin=MyWindow(window)
window.title('Login')
window.geometry("400x300+10+10")
window.mainloop()
