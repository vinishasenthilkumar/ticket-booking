#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import *
import pymysql
import re

connection = pymysql.connect(host='localhost',
                          user='root',
                          password='123456789',
                          database='tkinter')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS passenger_data
                      (
                       name VARCHAR(255),
                       age INT,
                       `from` VARCHAR(255),
                       `to` VARCHAR(255),
                       date VARCHAR(255),
                       gender VARCHAR(255),
                       adult INT,
                       children INT,
                       senior_citizen INT,
                       seat_type VARCHAR(255),
                       amount INT)''')


def clearfield():
    global b1,b2
    
    b1.delete(0,END)
    b2.delete(0,END)
    
def insert_data(connection,data):
    cursor=connection.cursor()
    cursor.execute("INSERT INTO passenger_data (name, age,`from`,`to`, date, gender, seat_type, adult, children, senior_citizen, amount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",data)
    connection.commit()
    print("user record inserted succesfully")




#signup page

def signup():

    a=tk.Tk()
    a.title('signup')
    username=Label(a, text='Username',width=25).grid(row=0)
    password=Label(a, text='Password',width=25).grid(row=1)
    retypepassword=Label(a, text='Re type Password',width=25).grid(row=2)
   
    a1 = Entry(a,width=30)
    a2 = Entry(a,width=30)
    a3 = Entry(a,width=30)
    a1.grid(row=0, column=1)
    a2.grid(row=1, column=1)
    a3.grid(row=2, column=1)
    
    button_submit=Button(a,text='submit',width=25,bg='green',fg='white',command=login)
    button_submit.grid(row=3,column=0)
    
    button_submit=Button(a,text='cancel',width=25,bg='red',fg='white',command=a.destroy)
    button_submit.grid(row=3,column=1)
    mainloop()
    
    #login page
    
    
def login():

    b=tk.Tk()
    b.title('Login')
    
    global b1,b2
    username=Label(b, text='Username').grid(row=0)
    password=Label(b, text='Password').grid(row=1)
    
    
    b1 = Entry(b,width=30)
    b2 = Entry(b,width=30,show='*')
    b1.grid(row=0, column=1)
    b2.grid(row=1, column=1)
    
    
    
    button_submit=Button(b,text='submit',width=25,bg='green',fg='white',command= submit)
    button_submit.grid(row=3,column=0)
    
    button_submit=Button(b,text='cancel',width=25,bg='red',fg='white',command= clearfield)
    button_submit.grid(row=3,column=1)
    
    
        
    
    
    mainloop()
    
    
    
    
#submit page
    
def submit():
    
    c=tk.Tk()
    c.title('submit')
    name=Label(c, text='Name :').grid(row=0)
    age=Label(c, text='Age :').grid(row=1)
    From=Label(c, text='From :').grid(row=2)
    To=Label(c,text='To :').grid(row=2,column=2)
    date=Label(c,text='Date :').grid(row=3)
    gender=Label(c,text='Gender :').grid(row=4)
    
    global e1,e2,e3,e4,e5,e6,var1,var2,var3,var4,var5,var6,var7
    global x,y,z
    
    var1 = IntVar()
    Checkbutton(c, text='Male', variable=var1).grid(row=5,column=1, sticky=W)
    var2 = IntVar()
    Checkbutton(c, text='Female', variable=var2).grid(row=6,column=1, sticky=W)
    
    seat=Label(c,text='seat :').grid(row=7)
    adult=Label(c,text='Adult :').grid(row=8)
    x= Spinbox(c,from_= 0, to = 100,width=10)
    x.grid(row=8,column=1)
    
    children=Label(c,text='Children :').grid(row=9)
    y= Spinbox(c,from_= 0, to = 100,width=10)
    y.grid(row=9,column=1)
    
    senior_citizen=Label(c,text='Senior citizen :').grid(row=10)
    z= Spinbox(c,from_= 0, to = 100,width=10)
    z.grid(row=10,column=1)
    
    seat_type=Label(c,text='seat_type :').grid(row=11)
    
   
    var3 = IntVar()
    Checkbutton(c, text='2s', variable=var3).grid(row=12,column=1, sticky=W)
    
    
    var4= IntVar()
    Checkbutton(c, text='sl', variable=var4).grid(row=13,column=1, sticky=W)
    
    
    var5= IntVar()
    Checkbutton(c, text='3AC', variable=var5).grid(row=14,column=1, sticky=W)
    
    
    var6 = IntVar()
    Checkbutton(c, text='2AC', variable=var6).grid(row=15,column=1, sticky=W)
    
    
    var7 = IntVar()
    Checkbutton(c, text='1AC', variable=var7).grid(row=16,column=1, sticky=W)
    
    amount=Label(c,text='Amount :').grid(row=17)
    
    button = tk.Button(c, text='submit', width=15,bg='green',fg='white', command=success)
    button.grid(row=18,column=1)
    
   

    e1 = Entry(c)
    e2 = Entry(c)
    e3 = Entry(c)
    e4 = Entry(c)
    e5 = Entry(c)
    e6 = Entry(c)
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=2, column=3)
    e5.grid(row=3, column=1)
    e6.grid(row=17, column=1)
    
    mainloop()
    
    
    


def success():
    
    print("var3:", var3.get())
    print("var4:", var4.get())
   


    # Get values from Entry widgets
    name = e1.get()
    age = e2.get()
    From = e3.get()
    To = e4.get()
    date = e5.get()
    gender = "Male" if var1.get() == 1 else "Female"
    seat_type = ", ".join(type for var, type in zip([var3, var4, var5, var6, var7], ['2s', 'sl', '3AC', '2AC', '1AC']) if var.get() == 1)
    adult = x.get()
    children = y.get()
    senior_citizen = z.get()
    amount = e6.get()
    
    data=(name, age,From, To, date, gender, seat_type, adult, children, senior_citizen, amount)
    insert_data(connection,data)
    
    show_success_message()

   


 # Connect to the mysql database
    
   

    # Create a table if not exists
    



# Start the Tkinter event loop
def show_success_message():
    s = tk.Tk()  #to create the main window
    s.title('submit_page')
    z ='Your booking is successfull'
    messageVar = Message(s, text = z)
    messageVar.config(bg='lightgreen')
    messageVar.pack( )
    
    mainloop()
    
    #front page

m = tk.Tk()  #to create the main window
m.title('ticket booking')
button = tk.Button(m, text='signup', width=15,bg='black',fg='white', command=signup) 
button.grid(row=0,column=0) #entha position la venum
button = tk.Button(m, text='log in', width=15,bg='black',fg='white', command=login)
button.grid(row=0,column=1)




m.mainloop() #run panna(used when your application is ready to run)
connection.close() #close the database connection
    
    
    


    


# In[ ]:





# In[4]:


#create database

import pymysql

connection=pymysql.connect(host='localhost',
                          user='root',
                          password='123456789',
                          database='tkinter')
                          
                          
mycursor = connection.cursor()
sql='create database if not exists tkinter'

mycursor.execute(sql)
mycursor.execute('show databases')

for x in mycursor:
    print(x)


# In[5]:


import pymysql

connection=pymysql.connect(host='localhost',
                          user='root',
                          password='123456789',
                          database='tkinter')
                          
                          
mycursor = connection.cursor()
mycursor.execute('create table password(username varchar(200),password int(8))')



# In[30]:


pip install pymysql


# In[ ]:


s = tk.Tk()  #to create the main window
   s.title('submit_page')
   z ='Your booking is successfull'
   messageVar = Message(s, text = z)
   messageVar.config(bg='lightgreen')
   messageVar.pack( )
   

