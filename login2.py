from tkinter import *
from tkinter import messagebox,messagebox
import ast
import sqlite3
import os
import requests
from tkcalendar import *
import database


login2=Tk()

login2.overrideredirect(1)
login2.title("BookYourFlight")
login2.geometry("800x600")
login2.resizable(0,0)
login2.wm_attributes("-transparentcolor", "grey")
#login2.iconbitmap("plane.ico")



bg = PhotoImage(file="C:/Users/HP/Desktop/PROJECT/images/air2.png")

af1 = Frame(login2, width=840, height=600)
af1.place(x=0, y=0)

my_label = Label(login2, bg="grey", image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

frm =Frame(login2,width=420,height=500, bg='#f7f9fc')
frm.place(x=205, y=70)

loginn = Label(frm, text="Create new Account", fg = "black",bg='#f7f9fc',font=("Microsoft Yahei UI light",24))
loginn.place(x=65, y=20)

Label(frm, text="Already Registered?", fg = "red",bg='#f7f9fc',font=("Microsoft Yahei UI light",11)).place(x=100, y=77)

#####---------------------------------------------

def move_app(e):
    login2.geometry(f'+{e.x_root}+{e.y_root}')

my_label.bind("<B1-Motion>", move_app)


def close():
    login2.destroy()

cross_img = PhotoImage(file="C:/Users/HP/Desktop/PROJECT/images/cross.png")
cross = Button(login2, border=0, bg = "#151E2E", image=cross_img, command=close)
cross.place(x=720, y=0, relheight=0.08, relwidth=0.06)

#####---------------------------------------------
def on_enter(e):
    id_entry.delete(0,'end')
def on_leave(e):
    if id_entry.get()=='':
        id_entry.insert(0,'ID')

id_entry = Entry(frm, text='ID', border=0,width=20,bg='#f7f9fc', font=("Microsoft Yahei UI light",12))
id_entry.place(x=105, y=135)
id_entry.insert(0,'ID')
id_entry.bind("<FocusIn>", on_enter)
id_entry.bind("<FocusOut>", on_leave)

Frame(frm, width=240, height=2, bg="black").place(x=95,y=155)


#####---------------------------------------------
def on_enter(e):
    username.delete(0,'end')
def on_leave(e):
    if username.get()=='':
        username.insert(0,'USERNAME')

username = Entry(frm, text='USERNAME', border=0,width=20,bg='#f7f9fc', font=("Microsoft Yahei UI light",12))
username.place(x=105, y=190)
username.insert(0,'USERNAME')
username.bind("<FocusIn>", on_enter)
username.bind("<FocusOut>", on_leave)

Frame(frm, width=240, height=2, bg="black").place(x=95,y=210)

#####---------------------------------------------

def on_enter(e):
    email_entry.delete(0,'end')
def on_leave(e):
    if email_entry.get()=='':
        email_entry.insert(0,'E-MAIL')

email_entry = Entry(frm, border=0,width=20, bg='#f7f9fc', font=("Microsoft Yahei UI light",12))
email_entry.place(x=105, y=245)
email_entry.insert(0,'E-MAIL')
email_entry.bind("<FocusIn>", on_enter)
email_entry.bind("<FocusOut>", on_leave)

Frame(frm, width=240, height=2, bg="black").place(x=95,y=265)

#####---------------------------------------------


def on_enter(e):
    phno_entry.delete(0,'end')
def on_leave(e):
    if phno_entry.get()=='+977 - ':
        phno_entry.insert(0,'+977 - ')

phno_entry = Entry(frm, border=0,width=20, bg='#f7f9fc', font=("Microsoft Yahei UI light",12))
phno_entry.place(x=105, y=305)
phno_entry.insert(0,'+977 - ')
phno_entry.bind("<FocusIn>", on_enter)
phno_entry.bind("<FocusOut>", on_leave)

Frame(frm, width=240, height=2, bg="black").place(x=95,y=325)

#####---------------------------------------------

def on_enter(e):
    password_entry.delete(0,'end')
def on_leave(e):
    if password_entry.get()=='':
        password_entry.insert(0,'PASSWORD')

password_entry = Entry(frm, border=0,width=20, bg='#f7f9fc', font=("Microsoft Yahei UI light",12))
password_entry.place(x=105, y=360)
password_entry.insert(0,'PASSWORD')
password_entry.bind("<FocusIn>", on_enter)
password_entry.bind("<FocusOut>", on_leave)

Frame(frm, width=240, height=2, bg="black").place(x=95,y=380)


#####---------------------------------------------

def signup():
    #conn = sqlite3.connect("NewSystem3.db")
    #c = conn.cursor()
    #c.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?)", [id.get(), username.get(), password.get(), email.get(), phno.get()])
    #conn.commit()
    #conn.close()

    id = id_entry.get()
    name = username.get()
    email = email_entry.get()
    phno = phno_entry.get()
    password = password_entry.get()

    if not (id and name and email and phno and password):
        messagebox.showerror('Error', 'Enter all fields.')
    elif database.id_exists(id):
        messagebox.showerror('Error', 'ID already exists.')
    else:
        database.insert_customer(id, name, email, phno, password)
        messagebox.showinfo('Success','Customer has been registerd.')
    #print("Account added")


loginl = Button(frm, text="Sign Up", border=0, fg="white", bg="#57a1f8",width=20, height=0, font=("Microsoft Yahei UI light",15,'bold'), command=signup)
loginl.place(x=90, y=410)

def logina():
    login2.destroy()
    import logintest


register = Button(frm, text="Log In", border=0, fg="#57a1f8", bg="#f7f9fc",width=6, height=0,cursor="hand2", font=("Microsoft Yahei UI light",11,'bold'),command=logina )
register.place(x=240, y=75)



login2.mainloop()
dash = Tk()
    
    