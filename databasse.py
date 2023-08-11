from tkinter import *

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Navigation Example")
        self.root.geometry("800x600")
        
        self.container = Frame(self.root)
        self.container.pack(fill="both", expand=True)
        
        self.frames = {}
        for FrameClass in (HomeFrame, ContactFrame, FeaturesFrame):
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=1, column=0, sticky="nsew")
        
        self.create_buttons()

    def create_buttons(self):
        button_frame = Frame(self.root)
        button_frame.pack(fill="x", side="top")

        self.buttons = []
        for FrameClass, text in zip((HomeFrame, ContactFrame, FeaturesFrame), ("Home", "Contact", "Features")):
            button = Button(button_frame, text=text, command=lambda frame_class=FrameClass: self.show_frame(frame_class))
            button.pack(side="top", pady=(10, 0))  # Add padding only above the button
            self.buttons.append(button)

        self.show_frame(HomeFrame)

        self.show_frame(HomeFrame)
    
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        
        for button in self.buttons:
            if frame_class == HomeFrame and button.cget("text") == "Home":
                button.config(bg="lightgray")
            elif frame_class == ContactFrame and button.cget("text") == "Contact":
                button.config(bg="lightblue")
            elif frame_class == FeaturesFrame and button.cget("text") == "Features":
                button.config(bg="lightgreen")
            else:
                button.config(bg="SystemButtonFace")

class HomeFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        label = Label(self, text="Home Frame Helllooo")
        label.pack(pady=10)

class ContactFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        label = Label(self, text="Contact Frame")
        label.pack(pady=10)

class FeaturesFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        label = Label(self, text="Features Frame")
        label.pack(pady=10)

if __name__ == "__main__":
    root = Tk()
    app = MyApp(root)
    root.mainloop()
