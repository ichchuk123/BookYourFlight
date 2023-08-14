from tkinter import Tk, ttk, Button, Label
from tkcalendar import Calendar  # Assuming you're using tkcalendar library

def get_dates():
    selected_date = cal.get_date()
    my_label.config(text="Your Date: " + selected_date)

# Create the main application window
root = Tk()
root.title("Calendar Example")
root.geometry("400x800")

# Create a frame
frm = Label(root)
frm.pack()

# Create the calendar widget
cal = Calendar(frm, font="Arial 15", selectmode='day', locale='en_US', cursor="hand2", year=2023, month=8, day=10)
cal.place(x=30, y=420)

# Create the "Get date" button
get_date = Button(frm, text="Get date", fg="#57a1f8", bg="white", font=("Microsoft Yahei UI light", 15, 'bold'), command=get_dates)
get_date.place(x=150, y=700)

# Create the label to display the selected date
my_label = Label(frm, fg="#57a1f8", bg="white", text="")
my_label.place(x=120, y=750)

# Start the GUI event loop
root.mainloop()

#    frm = Label(dash, height=810, width=1240, bg="#172233", image=frame)
        #    frm.place(x=270, y=25)
#
        #    normalLabel = Label(frm, text="Your ticket is here :", bg="white", border=0,font=("Microsoft Yahei UI light", 25, 'bold'))
        #    normalLabel.place(x=100, y=100)
#
#
        #    normalLabel = Label(frm, image=normal, bg="black", border=1)
        #    normalLabel.place(x=150, y=200)
#
        #    name = Label(normalLabel, bg="black", fg="white", height=1, text="Ram", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
        #    name.place(x=30, y=100)
#
        #    seat = Label(normalLabel, bg="black", fg="white", height=1, text="B17", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
        #    seat.place(x=165, y=100)
#
        #    boardingtime = Label(normalLabel, bg="black", fg="white", height=1, text="00:45", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
        #    boardingtime.place(x=160, y=165)
#
        #    flight = Label(normalLabel, bg="black", fg="white", height=1, text="12", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
        #    flight.place(x=35, y=165)
#
        #    date = Label(normalLabel, bg="black", fg="white", height=1, text="8/13/2023", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
        #    date.place(x=30, y=215)
#
        #    destination = Label(normalLabel, bg="black", fg="white", height=1, text="Pokhara", border=0, font=("Microsoft Yahei UI light", 10, 'bold'))
        #    destination.place(x=160, y=215)
        #
        #    my_label.place(x=150, y=550)
#
        #confirm = Button(frm, text="CONFIRM DATA", border=0, fg="white", bg="#57a1f8",width=15, height=0, font=("Microsoft Yahei UI light",18,'bold'), command=get_dates)
        #confirm.place(x=350, y=570)