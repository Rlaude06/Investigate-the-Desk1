from tkinter import *
import morse, cesar, base64

def change_win(id_win):
    global entry, result_str, param, buttons
    [i.destroy() for i in buttons]
    title = Label(win, text="Decode", fg="white", bg="black")
    title.pack()

    Label(win, text="Entrée", fg="white", bg="black").pack()
    entry = Entry(win, fg="white", bg="black")
    entry.pack()

    param_label = Label(win, text="Clé", fg="white", bg="black")
    param = Entry(win, fg="white", bg="black")

    if id_win == 4:
        param_label.pack()
        param.pack()

    enter_button = Button(win, text="Decode", fg="white", bg="black")
    enter_button.pack()
    result = Entry(win, state='readonly', readonlybackground='black', fg='white', width=30)
    result_str = StringVar()
    result_str.set('                                ')
    result.config(textvariable=result_str, relief='flat')
    result.pack()

    if id_win == 0:
        title.configure(text="Binaire", fg="white", bg="black")
        enter_button.configure(command=decode_bin)

    elif id_win == 1:
        title.configure(text="Héxadécimal", fg="white", bg="black")
        enter_button.configure(command=decode_hexa)
    
    
    elif id_win == 2:
        title.configure(text="Base64", fg="white", bg="black")
        enter_button.configure(command=decode_base64)

    elif id_win == 3:
        title.configure(text="Morse", fg="white", bg="black")
        enter_button.configure(command=decode_morse)

    else:
        title.configure(text="César", fg="white", bg="black")
        enter_button.configure(command=decode_cesar)


def decode_bin():
    entry_val = entry.get()
    result_str.set(str(int(entry_val, 2)))

def decode_hexa():
    entry_val = entry.get()
    result_str.set(str(int(entry_val, 16)))

def decode_base64():
    entry_val = entry.get()
    result_str.set(base64.b64decode(entry_val))

def decode_morse():
    entry_val = entry.get()
    result_str.set(morse.decode(entry_val))

def decode_cesar():
    entry_val = entry.get()
    entry_param = int(param.get())
    print(entry_val, entry_param)
    result_str.set(cesar.decode(entry_val, entry_param))

def run_decode():
    global win, buttons
    win = Toplevel(bg="black")
    buttons = [ 
        Button(win, text='Binaire', command=lambda:change_win(0), fg="white", bg="black"),
        Button(win, text='Héxadécimal', command=lambda:change_win(1), fg="white", bg="black"),
        Button(win, text='Base64', command=lambda:change_win(2), fg="white", bg="black"),
        Button(win, text='Morse', command=lambda:change_win(3), fg="white", bg="black"),
        Button(win, text='César', command=lambda:change_win(4), fg="white", bg="black")
    ]

    [i.pack() for i in buttons]


    win.mainloop()

if __name__=='__main__':
    run_decode()