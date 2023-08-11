from tkinter import *
from tkinter import messagebox,messagebox
import ast
import sqlite3
import os

if os.path.exists("NewSystem2.db"):
    conn = sqlite3.connect("NewSystem2.db")
else:
    conn = sqlite3.connect("NewSystem2.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS accounts
              (username text, password integer, email text, phno text)''')
    conn.commit()
    conn.close()

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
    username.delete(0,'end')
def on_leave(e):
    if username.get()=='':
        username.insert(0,'USERNAME')

username = Entry(frm, text="USERNAME", border=0,width=20,bg='#f7f9fc', font=("Microsoft Yahei UI light",12))
username.place(x=105, y=145)
username.insert(0,'USERNAME')
username.bind("<FocusIn>", on_enter)
username.bind("<FocusOut>", on_leave)

Frame(frm, width=240, height=2, bg="black").place(x=95,y=175)

#####---------------------------------------------

def on_enter(e):
    email.delete(0,'end')
def on_leave(e):
    if email.get()=='':
        email.insert(0,'E-MAIL')

email = Entry(frm, text="E-MAIL", border=0,width=20, bg='#f7f9fc', font=("Microsoft Yahei UI light",12))
email.place(x=105, y=200)
email.insert(0,'E-MAIL')
email.bind("<FocusIn>", on_enter)
email.bind("<FocusOut>", on_leave)

Frame(frm, width=240, height=2, bg="black").place(x=95,y=230)

#####---------------------------------------------


def on_enter(e):
    phno.delete(0,'end')
def on_leave(e):
    if phno.get()=='+977 - ':
        phno.insert(0,'+977 - ')

phno = Entry(frm, border=0,width=20, bg='#f7f9fc', font=("Microsoft Yahei UI light",12))
phno.place(x=105, y=255)
phno.insert(0,'+977 - ')
phno.bind("<FocusIn>", on_enter)
phno.bind("<FocusOut>", on_leave)

Frame(frm, width=240, height=2, bg="black").place(x=95,y=285)

#####---------------------------------------------

def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    if password.get()=='':
        password.insert(0,'PASSWORD')

password = Entry(frm, text="PASSWORD", border=0,width=20, bg='#f7f9fc', font=("Microsoft Yahei UI light",12))
password.place(x=105, y=315)
password.insert(0,'PASSWORD')
password.bind("<FocusIn>", on_enter)
password.bind("<FocusOut>", on_leave)

Frame(frm, width=240, height=2, bg="black").place(x=95,y=345)


#####---------------------------------------------

def signup():
    conn = sqlite3.connect("NewSystem2.db")
    c = conn.cursor()
    c.execute("INSERT INTO accounts VALUES (?, ?, ?, ?)", [username.get(), password.get(), email.get(), phno.get()])
    conn.commit()
    conn.close()

    print("Account added")


loginl = Button(frm, text="Sign Up", border=0, fg="white", bg="#57a1f8",width=20, height=0, font=("Microsoft Yahei UI light",15,'bold'), command=signup)
loginl.place(x=90, y=400)

def login():
    login2.destroy()
    import logintest

register = Button(frm, text="Log In", border=0, fg="#57a1f8", bg="#f7f9fc",width=6, height=0,cursor="hand2", font=("Microsoft Yahei UI light",11,'bold'),command=login )
register.place(x=240, y=75)

if __name__ == "__main__":
    signup()

login2.mainloop()