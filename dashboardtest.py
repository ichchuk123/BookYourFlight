
from tkinter import*
import requests
from tkcalendar import *
import sqlite3
import os

from login2 import username, password, email, phno

dash = Tk()

dash.title("Dashboard")
dash.attributes('-fullscreen', True)
dash.configure(bg="#172233")

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

    def edit_update_username():
        conn = sqlite3.connect("NewSystem2.db")
        c = conn.cursor()
        c.execute("UPDATE accounts SET username=?, password=?, emai=?, phno=?",[username.get(), password.get(), email.get(), phno.get()])
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


    Button(settingsfrm, text="Update", bg="#57a1f8", fg="white", border=0, font=("Uni Sans Heavy", 18), command=edit_update_username).place(x=450, y=750)
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
