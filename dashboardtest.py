from tkinter import*
import requests
from tkcalendar import *
import sqlite3
import os
import database
from tkinter import messagebox,messagebox
import random

def get_dates():
    selected_date = cal.get_date()
    my_label.config(border=0,text="Your Date: " + selected_date)

dash = Tk()

dash.title("Dashboard")
dash.attributes('-fullscreen', True)
dash.configure(bg="#172233")

#database.create_table()

api_key = '30d4741c779ba94c470ca1f63045390a'

yeti = PhotoImage(file="images/yeti.png")
shree = PhotoImage(file="images/shree.png")
tara = PhotoImage(file="images/tara.png")
saurya = PhotoImage(file="images/saurya.png")
buddha = PhotoImage(file="images/buddha.png")
line = PhotoImage(file="images/line.png")

normal = PhotoImage(file="images/yeti air ticket-1.png")

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

global normalLabel
normalLabel = Label(frm, image=normal, bg="black", border=1)
normalLabel.place(x=150, y=420)


global name
global seat
global boardingtime
global flight
global date
global destination

name = Label(normalLabel, bg="black", fg="white", height=1, text="ganga", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
name.place(x=30, y=100)

seat = Label(normalLabel, bg="black", fg="white", height=1, text="B17", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
seat.place(x=165, y=100)

boardingtime = Label(normalLabel, bg="black", fg="white", height=1, text="00:45", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
boardingtime.place(x=160, y=165)

flight = Label(normalLabel, bg="black", fg="white", height=1, text="12", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
flight.place(x=35, y=165)

date = Label(normalLabel, bg="black", fg="white", height=1, text="8/13/2023", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
date.place(x=30, y=215)

destination = Label(normalLabel, bg="black", fg="white", height=1, text="Pokhara", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
destination.place(x=160, y=215)



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


display_ = Label(weather_frame, text=weather, bg="#f2f2f2", fg="black", width=13, height=2, font=("Arial", 30, "bold"))
display_.place(x=375, y=45)

display2 = Label(weather_frame, text=celcius, bg="#f2f2f2", fg="black", width=4, height=1, font=("Arial", 55, "bold"))
display2.place(x=85, y=20)

celciusDisplay = Label(weather_frame, text="\u00b0C", bg="#f2f2f2", fg="black", width=2, height=1, font=("Arial", 40, "bold"))
celciusDisplay.place(x=260, y=35)

weather_frame.update()  # Update the frame to make sure its contents are displayed
#
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

        choose = Label(frm, text="Fill your personal details", bg="white", fg="#172233", border=0, font=("Microsoft Yahei UI light", 30))
        choose.place(x=75, y=50)

        nameLabel = Label(frm, text="Name :", width=10, bg="white", fg="black", border=0, font=("Microsoft Yahei UI light", 20))
        nameLabel.place(x=100, y=150)

        nameEntry = Entry(frm, width=20, bg="white", fg="black", border=1, font=("Microsoft Yahei UI light", 20))
        nameEntry.place(x=450, y=150)

        phnoLabel = Label(frm, text="Phone no :", width=10, bg="white", fg="black", border=0, font=("Microsoft Yahei UI light", 20))
        phnoLabel.place(x=100, y=250)

        phnoEntry = Entry(frm, width=20, bg="white", fg="black", border=1, font=("Microsoft Yahei UI light", 20))
        phnoEntry.place(x=450, y=250)

        departure_date = Label(frm, text="Choose your date:", width=20, bg="white", fg="black", border=0, font=("Microsoft Yahei UI light", 20))
        departure_date.place(x=50, y=350)

        boarding_time = Label(frm, text="Your Preffered Time:", width=20, bg="white", fg="black", border=0, font=("Microsoft Yahei UI light", 20))
        boarding_time.place(x=450, y=345)

        boarding_time_entry = Entry(frm, width=20, bg="white", fg="black", border=1, font=("Microsoft Yahei UI light", 20))
        boarding_time_entry.place(x=450, y=420)

        destinationLabel = Label(frm, text="Your Destination:", width=20, bg="white", fg="black", border=0, font=("Microsoft Yahei UI light", 20))
        destinationLabel.place(x=850, y=345)

        destination_entry = Entry(frm, width=20, bg="white", fg="black", border=1, font=("Microsoft Yahei UI light", 20))
        destination_entry.place(x=850, y=420)
       
        cal = Calendar(frm, font="Arial 15", selectmode='day', locale='en_US', cursor="hand2", year=2023,month=8,day=10)
        cal.place(x=30, y=420)
            
        get_date = Button(frm, text="Get date", fg="white", bg="#57a1f8", font=("Microsoft Yahei UI light", 15, 'bold'), command = get_dates)
        get_date.place(x=150, y=700)

        global my_label
        my_label = Label(frm, fg="#57a1f8", bg="white", text="")
        my_label.place(x=120, y=750)

        

        def confirm():
            frm = Label(dash, height=810, width=1240, bg="#172233", image=frame)
            frm.place(x=270, y=25) 

            global seatEntry
            info = '''"Congratulations, We have selected ticket 
            That suits best for you"'''

            global seatEntry

            displayLabel = Label(frm, text=info, width=35, bg="white", fg="red", border=0, font=("Uni Sans Thin CAPS", 22))
            displayLabel.place(x=270, y=90)

            ticketId = Label(frm, text="Ticket ID", width=10, bg="white", fg="black", border=0, font=("Uni Sans Thin CAPS", 22))
            ticketId.place(x=50, y=240) 

            conn = sqlite3.connect("NewSystem3.db")
            c = conn.cursor()
            c.execute('''SELECT flight_id from flightticket''')
            conn.commit()
            conn.close()

            ticket_random = random.randint(100,200)
            seat_random = random.randint(0,50)

            flightIdEntry = Label(frm, width=10, text=ticket_random, bg="white", fg="black", border=1, font=("Uni Sans Thin CAPS", 22))
            flightIdEntry.place(x=250, y=240) 

            seatLabel = Label(frm, text="Seat no.", width=10, bg="white", fg="black", border=0, font=("Uni Sans Thin CAPS", 22))
            seatLabel.place(x=50, y=320) 

            seatEntry = Label(frm, text=seat_random, width=10, bg="white", fg="black", border=1, font=("Uni Sans Thin CAPS", 22))
            seatEntry.place(x=250, y=320) 

            nameinfo = nameEntry.get()
            phnoinfo = phnoEntry.get()
            seatinfo = seatEntry.get()
            timeinfo = boarding_time_entry.get()
            dateinfo = my_label.get()
            destinationinfo = destination_entry.get()

            normalLabel = Label(frm, image=normal, bg="black", border=1)
            normalLabel.place(x=150, y=400)

            name = Label(normalLabel, bg="black", fg="white", height=1, text=nameinfo, border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
            name.place(x=30, y=100)

            seat = Label(normalLabel, bg="black", fg="white", height=1, text=seatinfo, border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
            seat.place(x=165, y=100)

            boardingtime = Label(normalLabel, bg="black", fg="white", height=1, text=timeinfo, border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
            boardingtime.place(x=160, y=165)

            flight = Label(normalLabel, bg="black", fg="white", height=1, text="12", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
            flight.place(x=35, y=165)

            date = Label(normalLabel, bg="black", fg="white", height=1, text="8/13/2023", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
            date.place(x=30, y=215)

            destination = Label(normalLabel, bg="black", fg="white", height=1, text=destinationinfo, border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
            destination.place(x=160, y=215)
 

            def confirmdata():
                if not (nameinfo and phnoinfo and seatinfo and timeinfo and dateinfo and destinationinfo):
                    messagebox.showerror("Error","Enter all your details")
                else:
                    database.add_flight(nameinfo, phnoinfo, seatinfo, timeinfo, dateinfo, destinationinfo)
                    messagebox.showinfo("Success", "Successfully updated")    

            confirmInfoLabel = Button(frm, text="Confirm", width=10, bg="#57a1f8", fg="black", border=0, font=("Uni Sans Thin CAPS", 22), command=confirmdata)
            confirmInfoLabel.place(x=500, y=600) 
       
        confirmLabel = Button(frm, text="Confirm Details", width=15, bg="#57a1f8", fg="white", border=0, font=("Microsoft Yahei UI light", 20), command=confirm)
        confirmLabel.place(x=500, y=700)
        

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

    
    Username = Label(settingsfrm, text="ganga", bg="#161616", fg="white", border=0, font=("Microsoft Yahei UI light", 25))
    Username.place(x=280, y=95)

    
    ########################################################################################################
    infoLabel = Label(settingsfrm, text="Personal Details", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 20))
    infoLabel.place(x=200, y=190)

    idLabel = Label(settingsfrm, text="Id no.", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
    idLabel.place(x=200, y=240)

    idEntry = Entry(settingsfrm, bg="#353536", fg="white", border=0, font=("Uni Sans Heavy", 20))
    idEntry.place(x=190, y=270)

    displayName = Label(settingsfrm, text="Username", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
    displayName.place(x=200, y=320)

    displayNameEntry = Entry(settingsfrm, bg="#353536", fg="white", border=0, font=("Uni Sans Heavy", 20))
    displayNameEntry.place(x=190, y=350)
    
    ########################################################################################################

    phoneName = Label(settingsfrm, text="Phone no.", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
    phoneName.place(x=200, y=410)

    displayPhoneEntry = Entry(settingsfrm, bg="#353536", fg="white", border=0, font=("Uni Sans Heavy", 20))
    displayPhoneEntry.place(x=190, y=440)

    ########################################################################################################

    emailName = Label(settingsfrm, text="Email", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
    emailName.place(x=200, y=510)

    displayEmailEntry = Entry(settingsfrm, bg="#353536", fg="white", border=0, font=("Uni Sans Heavy", 20))
    displayEmailEntry.place(x=190, y=540)

    ########################################################################################################

    passwordName = Label(settingsfrm, text="Password", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
    passwordName.place(x=200, y=610)

    displayPasswordEntry = Entry(settingsfrm,  bg="#353536", fg="white", border=0, font=("Uni Sans Heavy", 20))
    displayPasswordEntry.place(x=190, y=640)

    ########################################################################################################
    
    ########################################################################################################
    def edit_update():
        username = displayNameEntry.get()
        password = displayPasswordEntry.get()
        email = displayEmailEntry.get()
        phno = displayPhoneEntry.get()
        id = idEntry.get()
        if not (username and password and email and phno and id):
            messagebox.showerror("Error","Enter all your details")
        else:
            database.update_customer(username, password, email, phno, id)
            messagebox.showinfo("Success", "Successfully updated")
    
    def edit_delete():
        id = idEntry.get()
        if not (id):
            messagebox.showerror("Error","Enter your id")
        else:
            database.delete_customer(id)
            messagebox.showinfo("Success", "Successfully deleted")
            dash.destroy()
            import logintest

    Button(settingsfrm, text="Update", bg="#57a1f8", fg="white", border=0, font=("Uni Sans Heavy", 18), command=edit_update).place(x=170, y=720)
    Button(settingsfrm, text="Delete Your Account", bg="red", fg="white", border=0, width=16, font=("Uni Sans Heavy", 18), command=edit_delete).place(x=290, y=720)

    ########################################################################################################
    
    middleLabel = Label(settingsfrm, image=line, bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
    middleLabel.place(x=540, y=210, relwidth=0.1, relheight=0.64)

    ########################################################################################################

    flightInfo = Label(settingsfrm, text="Flight Details", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 20))
    flightInfo.place(x=750, y=190)

    flightIdLabel = Label(settingsfrm, text="Flight ID", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
    flightIdLabel.place(x=700, y=245)

    flightIdEntry = Entry(settingsfrm, bg="#353536", fg="white", border=0, font=("Uni Sans Heavy", 20))
    flightIdEntry.place(x=690, y=280)

    seatNumLabel = Label(settingsfrm, text="Seat no.", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
    seatNumLabel.place(x=700, y=365)

    seatNumEntry = Entry(settingsfrm, bg="#353536", fg="white", border=0, font=("Uni Sans Heavy", 20))
    seatNumEntry.place(x=690, y=395)
#
    boardingTimeLabel = Label(settingsfrm, text="Boarding Time", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
    boardingTimeLabel.place(x=700, y=480)

    boardingTimeEntry = Entry(settingsfrm, bg="#353536", fg="white", border=0, font=("Uni Sans Heavy", 20))
    boardingTimeEntry.place(x=690, y=520)

    departureDateLabel = Label(settingsfrm, text="Departure Date", bg="#48484a", fg="#dadadb", border=0, font=("Uni Sans Heavy", 15))
    departureDateLabel.place(x=700, y=600)

    departureDateEntry = Entry(settingsfrm, bg="#353536", fg="white", border=0, font=("Uni Sans Heavy", 20))
    departureDateEntry.place(x=690, y=640)


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
