from tkinter import *
from tkinter import messagebox,messagebox
import sqlite3
import os
import database
from tkinter import ttk



login = Tk()

login.overrideredirect(1)
login.title("BookYourFlight")
login.geometry("800x600")
login.resizable(0,0)
login.wm_attributes("-transparentcolor", "grey")

if os.path.exists("NewSystem3.db"):
    conn = sqlite3.connect("NewSystem3.db")
else:
    conn = sqlite3.connect("NewSystem3.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS accounts
              (username text, password integer, email text, phno text)''')
    conn.commit()
    conn.close()


top_label = Label(login, bg="black", width=1000, height=5)
top_label.pack()

bg = PhotoImage(file="C:/Users/HP/Desktop/PROJECT/images/air3.png")



af1 = Frame(login, width=840, height=600)
af1.place(x=0, y=0)

my_label = Label(login, border=0, bg="grey", image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)


#####---------------------------------------------

# Top label and close button

def move_app(e):
    login.geometry(f'+{e.x_root}+{e.y_root}')

my_label.bind("<B1-Motion>", move_app)


def close():
    login.destroy()

cross_img = PhotoImage(file="C:/Users/HP/Desktop/PROJECT/images/cross.png")
cross = Button(login, border=0, bg = "#151E2E", image=cross_img, command=close)
cross.place(x=720, y=0, relheight=0.08, relwidth=0.06)


#####---------------------------------------------

frm =Frame(login,width=320,height=330, bg='#f2f2f2')
frm.place(x=255, y=100)

loginn = Label(frm, text="Log In", fg = "#57a1f8",bg='#f2f2f2',font=("Microsoft Yahei UI light",25,'bold'))
loginn.place(x=105, y=15)

#####---------------------------------------------
def on_enter(e):
    username.delete(0,'end')
def on_leave(e):
    if username.get()=='':
        username.insert(0,'Username')

username = Entry(frm, text="Username", border=0,width=20,bg='#f2f2f2', font=("Microsoft Yahei UI light",15))
username.place(x=40, y=95)
username.insert(0,'Username')
username.bind("<FocusIn>", on_enter)
username.bind("<FocusOut>", on_leave)

Frame(frm, width=255, height=2, bg="black").place(x=30,y=125)

#####---------------------------------------------
def on_enter(e):
    password.delete(0,'end')
def on_leave(e):
    if password.get()=='':
        password.insert(0,'Password')


bg_eye1 = PhotoImage(file="C:/Users/HP/Desktop/PROJECT/images/hide.png")
bg_eye2 = PhotoImage(file="C:/Users/HP/Desktop/PROJECT/images/show.png")

def close_eye():
    eye_close = Button(frm, image=bg_eye1, border=0,bg='#f7f9fc', command=open_eye).place(x=240,y=135, relwidth=0.1, relheight=0.1)
    password.config(show="*")

def open_eye():
    eye_close = Button(frm, image=bg_eye2, border=0,bg='#f7f9fc', command=close_eye).place(x=240,y=135, relwidth=0.1, relheight=0.1)
    password.config(show="")

password = Entry(frm, text="Password1234", border=0,width=20,bg='#f2f2f2', font=("Microsoft Yahei UI light",15), show="*")
password.place(x=40, y=140)
password.insert(0,'Password')
password.bind("<FocusIn>", on_enter)
password.bind("<FocusOut>", on_leave)

Frame(frm, width=255, height=2, bg="black").place(x=30,y=170)


eye_close = Button(frm, image=bg_eye1, border=0,bg='#f7f9fc', command=close_eye).place(x=240,y=135, relwidth=0.1, relheight=0.1)

#####---------------------------------------------
def logN():
    database.fetch_data()
    login.destroy()
    import dashboardtest


loginl = Button(frm, text="Log In", border=0, fg="white", bg="#57a1f8",width=20, height=0, font=("Microsoft Yahei UI light",15,'bold'), command=logN)
loginl.place(x=35, y=190)

label = Label(frm, text="New User", fg="black", bg="#f2f2f2", font=("Microsoft Yahei UI light",13))
label.place(x=80, y=267) 

def register():
    login.destroy()
    import login2

register1 = Button(frm, text="Register", border=0, fg="#57a1f8", bg="#f2f2f2",width=8, height=0,cursor="hand2", font=("Microsoft Yahei UI light",13,'bold'),command=register)
register1.place(x=155, y=264)

login.mainloop()


