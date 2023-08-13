from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
import random
import glob


class Gui:
    def __init__(self, mainwin):
        self.counter = 0
        self.mainwin = mainwin
        self.mainwin.title('Tkinter PIcture Frame')
        self.mainwin.state('zoomed')

        self.frame = Frame(mainwin)

        self.img = Label(self.frame)

        self.frame.place(relheight=0.6, relwidth=0.9, relx=0.05, rely=0.2)
        self.img.place(x=0, y=-20)
        
        self.pic()
        self.setup_first_gui()

        # Call the function to set up the GUI of the first code snippet
        


    def pic(self):
        self.pic_list = []

        for name in glob.glob(r"C:/Users/HP/Desktop/PROJECT/image/*"):
            val = name
            self.pic_list.append(val)

        if not self.pic_list:
            return

        self.file = self.pic_list[self.counter]
        self.load = Image.open(self.file)

        self.pic_width = self.load.size[0]
        self.pic_height = self.load.size[1]

        self.real_aspect = self.pic_width / self.pic_height
        self.cal_width = int(self.real_aspect * 600)

        self.load2 = self.load.resize((self.cal_width, 600))
        self.render = ImageTk.PhotoImage(self.load2)
        self.img.config(image=self.render)
        self.img.image = self.render

        self.counter = (self.counter + 1) % len(self.pic_list)  # Reset counter to 0 when it reaches the end
        self.mainwin.after(2000, self.pic)


    def setup_first_gui(self):
        # The code for the first GUI, as in the first code snippe

        home = self.mainwin
        home.attributes('-fullscreen', True)
        home.configure(bg="white")


        Label(home, text = "______________________________________________________________________________________________",font=("Microsoft Yahei UI light",35), fg="#57a1f8", bg="white").place(x=0,y=90)

        heading1 = Label(home, text="Book Your Flight", bg="white", font=("Microsoft Yahei UI light",15))
        heading1.place(x=230,y=50)

        heading2 = Label(home, text="Airlines Reservation System", bg="white", font=("Microsoft Yahei UI light",15))
        heading2.place(x=190,y=85)


        logo = PhotoImage(file="C:/Users/HP/Desktop/PROJECT/images/plane.png")

        logo_label = Label(home, border=0, image=logo)
        logo_label.place(x=40, y=15, relwidth=0.1, relheight=0.15)

        def log():
            home.destroy()
            import login2

        loginb = Button(home, text="Log In", border=0, fg="white", bg="#57a1f8",width=10, height=0, font=("Microsoft Yahei UI light",18,'bold'), command=log)
        loginb.place(x=1275, y=50)

        
        ####################################################

        text = Label(home, text=" ''Your Adventure Begins Now !!''\n \n- Book Your Flight ", border=0, fg="black", bg="white",width=50, height=0, font=("Microsoft Yahei UI light",22))
        text.place(x=310, y=700)

        ####################################################

        header = Label(home, text=" ", bg="#23395d", width = 200,font=("Microsoft Yahei UI light",10))
        header.place(x=0,y=0)

        home.mainloop()


####################################################

if __name__ == "__main__":
    mainwin = Tk()
    myprog = Gui(mainwin)
    mainwin.mainloop()
