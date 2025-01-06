import sys
import os
from tkinter import *
import mysql.connector
from datetime import date

mydb=mysql.connector.connect(host="localhost",user="admin",passwd="admin",database="driverhire")
mycur=mydb.cursor()
window=Tk()

window.title("Driver Hire - Options Menu")
window.geometry('600x500')

def driver():
    os.system('python driverprofile.py')

def customer():
    os.system('python drivercustomer.py')

def booking():
    os.system('python driverbooking.py')

def allotment():
    os.system('python driverallotment.py')

def cancellation():
    os.system('python drivercancellation.py')

def checktiming():
    os.system('python timingsqlinjection.py')

def allattacks():
    os.system('python allsqlinjection.py')


def run2():
    #piggysqlinjection
    sqlst="select * from diabetictocardiac"
    mycur.execute(sqlst)
    res=mycur.fetchall()
    if res:
        for row in res:
            print(row)
            print("\n")
    else:
            print('Patient Not Found')
           
def logout():
    window.destroy()

lbl17=Label(window, text="NS Drivers Desk, Pollachi")
lbl17.place(x=200,y=20)
lbl7=Label(window, text='DRIVER HIRING SYSTEM')
lbl7.place(x=200, y=50)
lbl6=Label(window, text='Date : ' + str(date.today()))
lbl6.place(x=200, y=100)


btn2 = Button(window, text="Driver Profile", bg="black", fg="white",command=driver,height = 2, width = 30)
btn2.place(x=200, y=150)

btn3 = Button(window, text="Customer Profile", bg="black", fg="white",command=customer,height = 2, width = 30)
btn3.place(x=200, y=200)

btn4 = Button(window, text="Driver Booking", bg="black", fg="white",command=booking,height = 2, width = 30)
btn4.place(x=200, y=250)

btn5 = Button(window, text="Driver Allotment", bg="black", fg="white",command=allotment,height = 2, width = 30)
btn5.place(x=200, y=300)

btn6 = Button(window, text="Booking Cacenllation", bg="black", fg="white",command=cancellation,height = 2, width = 30)
btn6.place(x=200, y=350)

btn7 = Button(window, text="Driver Allotment details report", bg="black", fg="white",command=allattacks,height = 2, width = 30)
btn7.place(x=200, y=400)

btn8 = Button(window, text="Logout", bg="black", fg="white",command=logout,height = 2, width = 30)
btn8.place(x=200, y=450)



window.mainloop()
