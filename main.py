from Hr import Hr
from tkinter import *
from PIL import Image,ImageTk


class Main():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry("500x350")
        self.root.config(bg="#fedbd0")
        self.root.title("HRMD Server")
        pic = "Pictures/logo.png"
        logo = Image.open(pic)
        final = logo.resize((120,100))
        self.logo = ImageTk.PhotoImage(final)
        
        header = Frame(self.root, width=500, height=100, bg="#fedbd0")
        footer = Frame(self.root, width=500, height=100, bg="#fedbd0")
        body = Frame(self.root, width=500, height=300, bg="#fedbd0")
        
        labelT = Label(header, text="HUMAN RESOURCES\nMANAGEMENT DEPARTMENT", width=38, bg="#fedbd0", fg="#442c2e", font=("Arial", 16, "bold"))
        labelS = Label(body, text="Choose Option", bg="#fedbd0", font=("Arial", 15))
        
        header.grid(row=0, column=0, columnspan=2)
        labelT.pack(pady=20)
        
        body.grid(row=1, column=0, columnspan=2)
        logopic = Label(body,image=self.logo, bg="#fedbd0").pack()
        labelS.pack(padx=10)
        
        footer.grid(row=2, column=0, columnspan=2)
        
    def start(self):
        self.root.mainloop()

start = Main()
start.start()
