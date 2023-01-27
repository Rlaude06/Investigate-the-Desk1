import os
from tkinter import *
from PIL import Image, ImageTk

import os
import radio, image_opener, notes, decode, faille, default
from positions import check_click


win= Tk()

win.attributes('-fullscreen', True)

w, h = win.winfo_screenwidth(), win.winfo_screenheight()


def get_img_widget(src):
    img = Image.open(src).resize((w, h))
    img = ImageTk.PhotoImage(image=img, master=win)
    return img


backgrounds = {
    "black": get_img_widget("img/black.png"), 
    "default": get_img_widget("img/back3.png"),
 }

intro_strs = [open("txt0", encoding="utf-8").read(),open("txt1", encoding="utf-8").read(), open("txt2", encoding="utf-8").read()]

current_page=0

def update_image():
    global current_page
    current_page+=1
    if current_page==3:
        can.itemconfig(image_container,image=backgrounds["default"])  
        info_text.destroy()
        next_button.destroy()
    else:
        info_text.config(text=intro_strs[current_page])




can = Canvas(win, highlightthickness=0)
can.pack(fill='both', expand=1)

def imprimante():
    win2 = Toplevel()
    win2.title("Imprimante")
    Label(win2, text="Il semblerai qu'un fichier contenu dans "+os.path.abspath("files/")+"\nsoit protégé par un mot de passe rendant l'impression impossible...").pack() # 6614 // 1100111010110 // 101001
    win2.mainloop()

def handle_click(event):
    if current_page!=3:
        return

    x, y = event.x, event.y
    new_win_id = check_click(x,y,w,h)

    if not new_win_id:
        return
    
    if new_win_id=="radio":
        radio.run_radio()

    elif new_win_id=="notes":
        notes.run_notes()

    elif new_win_id=="decode":
        decode.run_decode()

    elif new_win_id=="faille":
        faille.run_faille()

    elif new_win_id=="imprimante":
        imprimante()

    elif new_win_id in ("poeme", "phone", "ordi", "chocolat"):
        image_opener.open_image(new_win_id)



image_container = can.create_image(0,0, anchor="nw",image=backgrounds["black"])

can.bind("<Button-1>", handle_click)


close_button = Button(can, text="Quitter le jeu", bg="black", fg="red", command=win.destroy, highlightthickness=0, font='Helvetica 18 bold')
close_button.pack(side=BOTTOM)



next_button = Button(can, text="Suivant", bg="black", fg="white", command=update_image)
next_button.pack(side=BOTTOM)


info_text = Label(can, text = intro_strs[0], fg="white", bg="black", justify=LEFT, font=("Helvetica",30))
info_text.pack(side=BOTTOM)
win.mainloop()