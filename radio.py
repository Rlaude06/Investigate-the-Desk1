from tkinter import *

def run_radio():
    win = Toplevel()
    win.title("Radio")

    img = PhotoImage(file="img/radio.png")

    width, height = img.width(), img.height()
    print(width, height)
    can = Canvas(win,  width=width, height=height, bd=0, highlightthickness=0, relief='ridge')

    can.pack()
    can.create_image(0, 0, image=img, anchor=NW)
    win.config(bg = '#add123')

    def show_code():
        code = float(entry_number.get())
        if code == 152.4:
            result_str.set("La radio émets des bip parfois cours parfois long : ... -.- .... ..")
        else:
            result_str.set("............ La radio grésille vous ne semblez pas être sur la bonne fréquence")

    var_d = DoubleVar(value=107.7)
    entry_number = Spinbox(win, from_= .0, to = 200.0,width=5, increment=.1,
        textvariable=var_d, bg="#C9BCAC", bd=0, highlightthickness=0, relief='ridge')

    mhz =Label(win,text="MHz :", bg="#C9BCAC")
    can.create_window(360, 210, anchor='nw', window=mhz) 

    can.create_window(400,210, anchor="nw", window=entry_number)

    play = Button(win, text = "►", command = show_code, anchor = 'w', bd=0, highlightthickness=0, relief='ridge', bg="#B1A184", font=("bold", 15), fg="white")
    can.create_window(385, 230, anchor='nw', window=play) 

    
    result = Label(win, text="", fg="black")
    result = Entry(win, state='readonly', readonlybackground='white', fg='black', width=100)
    result_str = StringVar()
    result_str.set('                                ')
    result.config(textvariable=result_str, relief='flat')

    can.create_window(0,400, anchor="nw", window=result)
    win.mainloop()

if __name__=="__main__":
    run_radio()