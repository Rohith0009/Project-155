from tkinter import *
import random

root = Tk()
root.geometry("1600x1600")
root.title("Color Changer")

colors = ["blue","red","green","yellow","cyan","Pink","purple","teal","orange","brown"]

def color_changer():
    root.configure(bg=random.choice(colors))

MrChanger = Button(root, text="Chnage Color", command=color_changer)
MrChanger.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()