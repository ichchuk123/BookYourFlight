from tkinter import *
from tkinter import messagebox,messagebox
import ast
import sqlite3
import os
import requests
from tkcalendar import *

login2=Tk()

login2.overrideredirect(1)
login2.title("BookYourFlight")
login2.geometry("800x600")
login2.resizable(0,0)
login2.wm_attributes("-transparentcolor", "grey")
#login2.iconbitmap("plane.ico")

if os.path.exists("NewSystem2.db"):
    conn = sqlite3.connect("NewSystem2.db")
else:
    conn = sqlite3.connect("NewSystem2.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS accounts
              (username text, password integer, email text, phno text)''')
    conn.commit()
    conn.close()

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

def logina():
    login2.destroy()
    
    login = Tk()

    login.overrideredirect(1)
    login.title("BookYourFlight")
    login.geometry("800x600")
    login.resizable(0,0)
    login.wm_attributes("-transparentcolor", "grey")

    if os.path.exists("NewSystem2.db"):
        conn = sqlite3.connect("NewSystem2.db")
    else:
        conn = sqlite3.connect("NewSystem2.db")
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
    global frm
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

    username = Entry(frm, border=0,width=20,bg='#f2f2f2', font=("Microsoft Yahei UI light",15))
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

    password = Entry(frm, border=0,width=20,bg='#f2f2f2', font=("Microsoft Yahei UI light",15), show="*")
    password.place(x=40, y=140)
    password.insert(0,'Password')
    password.bind("<FocusIn>", on_enter)
    password.bind("<FocusOut>", on_leave)

    Frame(frm, width=255, height=2, bg="black").place(x=30,y=170)


    eye_close = Button(frm, image=bg_eye1, border=0,bg='#f7f9fc', command=close_eye).place(x=240,y=135, relwidth=0.1, relheight=0.1)

    #####---------------------------------------------
    def logN():
        conn = sqlite3.connect("NewSystem2.db")
        c = conn.cursor()
        c.execute("SELECT * FROM accounts WHERE username=? AND password=?", [username.get(), password.get()])
        if c.fetchone() is None:
            
            print("Incorrect credentials")
            Label(frm, text="Invalid Data", bg="#f2f2f2", fg="red", width=15, height=1, font=("Microsoft Yahei UI light",10)).place(x=35, y=242)
            Button(frm, text="Not registered", border=0, fg="red", bg="#f2f2f2",width=15, height=0, font=("Microsoft Yahei UI light",10,'bold')).place(x=135, y=240)
        else:
            print("Logged In!")
            login.destroy()
            dash = Tk()
            dash.title("Dashboard")
            dash.attributes('-fullscreen', True)
            dash.configure(bg="#172233")

            

            frm =Frame(login,width=320,height=330, bg='#f2f2f2')
            frm.place(x=255, y=100)

            if os.path.exists("NewSystem.db"):
                conn = sqlite3.connect("NewSystem.db")
            else:   
                conn = sqlite3.connect("NewSystem.db")
                c = conn.cursor()
                c.execute('''CREATE TABLE accounts
                          (name text, password integer, email text, phno text )''')
                conn.commit()
                conn.close()

            api_key = '30d4741c779ba94c470ca1f63045390a'

            yeti = PhotoImage(file="images/yeti.png")
            shree = PhotoImage(file="images/shree.png")
            tara = PhotoImage(file="images/tara.png")
            saurya = PhotoImage(file="images/saurya.png")
            buddha = PhotoImage(file="images/buddha.png")

            normal = PhotoImage(file="images/pd.png")

            frame = PhotoImage(file="images/frame.png")
            frm = Label(dash, height=810, width=1240, bg="#172233", image=frame)
            frm.place(x=270, y=25)

            cal = Calendar(frm, font="Arial 18", selectmode='none', locale='en_US', cursor="hand2", year=2023,month=7,day=31)

            welcome = Label(frm, text="Welcome to", bg="white", fg="#172233", font=("Microsoft Yahei UI light", 15))
            welcome.place(x=75, y=45)

            db_label = Label(frm, text="Dashboard !!", bg="white", fg="#172233", font=("Microsoft Yahei UI light", 30, "bold"))
            db_label.place(x=60, y=75)

            ofrm = PhotoImage(file="images/ofrm.png")
            afrm = Label(frm, image=ofrm, width=1050, height=180, bg="white")
            afrm.place(x=100, y=150)

            ticketLabel = Label(frm, text="Your ticket :", bg="white", fg="#172233", font=("Microsoft Yahei UI light", 20, "bold"))
            ticketLabel.place(x=100, y=350)

            normalLabel = Label(frm, image=normal, bg="black", border=1)
            normalLabel.place(x=150, y=420)



            fm1 = Label(afrm, bg="#f2f2f2", width=130, height=10)
            fm1.place(x=65, y=10)

            location = "kathmandu"
            weather_data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&APPID={api_key}")

            if weather_data.json()['cod'] == '404':
                print("No City Found")
            else:
                weather = weather_data.json()['weather'][0]['main']
                temp = round(weather_data.json()['main']['temp'])
                celcius1 = (temp - 32) * 5 / 9
                celcius = round(celcius1, 1)


            weather_frame = Frame(afrm, bg="#f2f2f2", width=1050, height=180)
            weather_frame.place(x=0, y=0)

            location1 = Label(weather_frame, text=("Kathmandu, Nepal"), bg="#f2f2f2", fg="black", width=20, height=2, font=("Arial", 20, "bold"))
            location1.place(x=40, y=100)

            weather_icon_frame = Frame(weather_frame, bg="#f2f2f2", width=120, height=120)
            weather_icon_frame.place(x=630, y=10)

            if weather == "Clouds":
                cloud1 = PhotoImage(file="images/cloud2.png")
                cloud1_label = Label(weather_icon_frame, bg="#f2f2f2", image=cloud1)
                cloud1_label.place(x=10, y=20, relheight=1, relwidth=1)
            elif weather == "Rain":
                rain_icon = PhotoImage(file="images/rain.png")
                rain_label = Label(weather_icon_frame, bg="#f2f2f2", image=rain_icon)
                rain_label.place(x=0, y=0, relheight=1, relwidth=1)

            display_ = Label(weather_frame, text=weather, bg="#f2f2f2", fg="black", width=10, height=2, font=("Arial", 30, "bold"))
            display_.place(x=375, y=45)

            display2 = Label(weather_frame, text=celcius, bg="#f2f2f2", fg="black", width=4, height=1, font=("Arial", 55, "bold"))
            display2.place(x=85, y=20)

            celciusDisplay = Label(weather_frame, text="\u00b0C", bg="#f2f2f2", fg="black", width=2, height=1, font=("Arial", 40, "bold"))
            celciusDisplay.place(x=260, y=35)

            weather_frame.update()  # Update the frame to make sure its contents are displayed

            logo = PhotoImage(file="images/planebg1.png")
            logo_label = Label(dash, bg="#172233", image=logo)
            logo_label.place(x=50, y=50, relwidth=0.1, relheight=0.1)



            ########################################################################################################

                    # functions for opening new window

            def open_dashboard():
                frm = Label(dash, height=810, width=1240, bg="#172233", image=frame)
                frm.place(x=270, y=25)

            dashboard = Button(dash, text="Dashboard", bg="#172233", fg="white", border=0, font=("Sans Serif", 16), command=open_dashboard)
            dashboard.place(x=75, y=250)

            def ticket_book():
                frm = Label(dash, height=810, width=1240, bg="#172233", image=frame)
                frm.place(x=270, y=25)  

                chooseAirline = Label(frm, text="Choose your airline :", bg="white", fg="#172233", border=0, font=("Microsoft Yahei UI light", 30))
                chooseAirline.place(x=75, y=50)

                def open_window():
                    frm = Label(dash, height=810, width=1240, bg="#172233", image=frame)
                    frm.place(x=270, y=25)

                    choose = Label(frm, text="Choose date and time for your booking :", bg="white", fg="#172233", border=0, font=("Microsoft Yahei UI light", 30))
                    choose.place(x=75, y=50)
            #       
                    global cal
                    cal = Calendar(frm, font="Arial 18", selectmode='day', locale='en_US', cursor="hand2", year=2023,month=8,day=10)
                    cal.place(x=210, y=150)
            #
                    timeLabel = Label(frm, text="Time :", width=5, bg="black", fg="white", border=0, font=("Microsoft Yahei UI light", 15))
                    timeLabel.place(x=310, y=460)
            #
                    time = Entry(frm, bg="black", fg="white", width=10, border=0, font=("Microsoft Yahei UI light", 15))
                    time.place(x=380, y=460)
                    my_label = Label(frm, fg="#57a1f8", bg="white", text="")
                #
                    def get_dates():
                        if time.get()==False:
                            Label(frm, text="You must enter time", font=("Microsoft Yahei UI light", 15, 'bold')).place(x=150, y=520)
                        my_label.config(text="Your Date: " + cal.get_date() + " and time: " + time.get(), font=("Microsoft Yahei UI light", 15, 'bold'))

                        frm = Label(dash, height=810, width=1240, bg="#172233", image=frame)
                        frm.place(x=270, y=25)

                        normalLabel = Label(frm, text="Your ticket is here :", bg="white", border=0,font=("Microsoft Yahei UI light", 25, 'bold'))
                        normalLabel.place(x=100, y=100)


                        normalLabel = Label(frm, image=normal, bg="black", border=1)
                        normalLabel.place(x=150, y=200)



                        my_label.place(x=150, y=550)


                #
                    confirm = Button(frm, text="CONFIRM DATA", border=0, fg="white", bg="#57a1f8",width=15, height=0, font=("Microsoft Yahei UI light",18,'bold'), command=get_dates)
                    confirm.place(x=350, y=570)




                yetiLabel = Button(frm, border=0, bg="white", image=yeti, command=open_window)
                yetiLabel.place(x=50, y=140, relheight=0.19, relwidth=0.32)

                sauryaLabel = Button(frm, border=0, bg="white", image=saurya, command=open_window)
                sauryaLabel.place(x=650, y=190, relheight=0.15, relwidth=0.3)

                taraLabel = Button(frm, border=0, bg="white", image=tara, command=open_window)
                taraLabel.place(x=320, y=330, relheight=0.2, relwidth=0.4)

                shreeLabel = Button(frm, border=0, bg="white", image=shree, command=open_window)
                shreeLabel.place(x=50, y=530, relheight=0.2, relwidth=0.32)

                buddhaLabel = Button(frm, border=0, bg="white", image=buddha, command=open_window)
                buddhaLabel.place(x=650, y=530, relheight=0.2, relwidth=0.4)


            customers = Button(dash, text="Book a ticket", bg="#172233", fg="white", border=0, font=("Sans Serif", 16), command = ticket_book)
            customers.place(x=75, y=350)


            Label(dash, text="____________________", bg="#172233", fg="white", border=0, font=("Sans Serif", 12)).place(x=45, y=550)

            def open_settings():
            
                global setting

                global settingsfrm
                setting = PhotoImage(file="images/settingsfrm.png")
                settingsfrm = Label(dash, height=810, width=1240, bg="#172233", image=setting)
                settingsfrm.place(x=270, y=25)


                topLabel = Label(settingsfrm, bg="#161616", fg="white", border=0, height=5, width=100, font=("Microsoft Yahei UI light", 20, 'bold'))
                topLabel.place(x=-5, y=-5)
            #
                global pp

                pp = PhotoImage(file="images/logo.png")
                pp_Label = Label(topLabel, bg="#161616", image=pp)
                pp_Label.place(x=120, y=55, relheight=0.6, relwidth=0.1)


                Username = Label(settingsfrm, text="Ram", bg="#161616", fg="white", border=0, font=("Microsoft Yahei UI light", 25))
                Username.place(x=280, y=95)

                def edit_update():
                    conn = sqlite3.connect("NewSystem2.db")
                    c = conn.cursor()
                    if username.get() == displayNameEntry.get() and password.get() == displayPasswordEntry.get():
                        c.execute("UPDATE accounts SET username=?, password=?, email=?, phno=?",[displayNameEntry.get(), displayPasswordEntry.get(), displayEmailEntry.get(), displayPhoneEntry.get()])
                    
                    conn.commit()
                    conn.close()


                ########################################################################################################

                displayName = Label(settingsfrm, text="Username", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
                displayName.place(x=200, y=210)

                displayNameEntry = Entry(settingsfrm, bg="#48484a", fg="white", border=0, font=("Uni Sans Heavy", 20))
                displayNameEntry.place(x=200, y=240)



                ########################################################################################################

                phoneName = Label(settingsfrm, text="Phone no.", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
                phoneName.place(x=200, y=330)

                displayPhoneEntry = Entry(settingsfrm, bg="#48484a", fg="white", border=0, font=("Uni Sans Heavy", 20))
                displayPhoneEntry.place(x=200, y=360)



                ########################################################################################################

                emailName = Label(settingsfrm, text="Email", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
                emailName.place(x=200, y=450)

                displayEmailEntry = Entry(settingsfrm, bg="#48484a", fg="white", border=0, font=("Uni Sans Heavy", 20))
                displayEmailEntry.place(x=200, y=480)


                ########################################################################################################

                passwordName = Label(settingsfrm, text="Password", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
                passwordName.place(x=200, y=570)

                displayPasswordEntry = Entry(settingsfrm,  bg="#48484a", fg="white", border=0, font=("Uni Sans Heavy", 20))
                displayPasswordEntry.place(x=200, y=600)


                Button(settingsfrm, text="Update", bg="#57a1f8", fg="white", border=0, font=("Uni Sans Heavy", 18), command=edit_update).place(x=450, y=750)
                Button(settingsfrm, text="Delete", bg="red", fg="white", border=0, font=("Uni Sans Heavy", 18)).place(x=600, y=750)

            settings = Button(dash, text="Settings", bg="#172233", fg="white", border=0, font=("Sans Serif", 16), command=open_settings)
            settings.place(x=75, y=450)

            def signout():
                dash.destroy()
                import logintest

            logout = Button(dash, text="Sign Out", bg="#172233", fg="white", border=0, font=("Sans Serif", 16), command=signout)
            logout.place(x=75, y=600)

            def close():
                dash.destroy()

            cross_img = PhotoImage(file="images/cross.png")
            cross = Button(dash, border=0, bg="#172233", image=cross_img, command=close)
            cross.place(x=0, y=0, relheight=0.08, relwidth=0.06)


            dash.mainloop()


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


register = Button(frm, text="Log In", border=0, fg="#57a1f8", bg="#f7f9fc",width=6, height=0,cursor="hand2", font=("Microsoft Yahei UI light",11,'bold'),command=logina )
register.place(x=240, y=75)

if __name__ == "__main__":
    signup()

login2.mainloop()
dash = Tk()
    
    