from tkinter import *
from PIL import Image, ImageTk

def open_image(name):
    win = Toplevel()
    win.title(name)
    img = PhotoImage(file="img/%s.png" % name)

    w, h = img.width(), img.height()
    img_lab = Label(win)
    img_lab.config(image=img)
    img_lab.pack()
    win.minsize(w,h)
    win.maxsize(w,h)
    win.mainloop()

