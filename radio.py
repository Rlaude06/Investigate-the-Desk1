from tkinter import *

def run_radio():
	# Créer une fenêtre avec un titre Radio
    win = Toplevel()
    win.title("Radio")

	# Ouvrir image radio et définir taille du canvas comme corrspondant à sa résolution
    img = PhotoImage(file="img/radio.png")
    width, height = img.width(), img.height()
    can = Canvas(win,  width=width, height=height, bd=0, highlightthickness=0, relief='ridge')
    can.pack()

	# Afficher une image de radio
    can.create_image(0, 0, image=img, anchor=NW)
    win.config(bg = '#add123')

	# Retourne le code morse dans la zone de texte si la fréquence réglée est la bonne
    def show_code():
        code = float(entry_number.get())
        if code == 152.4:
            result_str.set("La radio émets des bip parfois cours parfois long : ... -.- .... ..")
        else:
            result_str.set("............ La radio grésille vous ne semblez pas être sur la bonne fréquence")

	# Créer une variable double de tkinter modifiable par un widget
    var_d = DoubleVar(value=107.7)

	# Créer une entrée avec des flèches pour monter et descendre la valeur
    entry_number = Spinbox(win, from_= .0, to = 200.0,width=5, increment=.1,
        textvariable=var_d, bg="#C9BCAC", bd=0, highlightthickness=0, relief='ridge')

	# Zone de text affichant MHz
    mhz =Label(win,text="MHz :", bg="#C9BCAC")
    can.create_window(360, 210, anchor='nw', window=mhz) 

	# Affiche l'entrée numérique
    can.create_window(400,210, anchor="nw", window=entry_number)

	# Créer un bouton pour exécuter show_code
    play = Button(win, text = "►", command = show_code, anchor = 'w', bd=0, highlightthickness=0, relief='ridge', bg="#B1A184", font=("bold", 15), fg="white")
    can.create_window(385, 230, anchor='nw', window=play) 

    # Zone de texte où est affiché le code morse
    result = Label(win, text="", fg="black")
    result = Entry(win, state='readonly', readonlybackground='white', fg='black', width=100)
    result_str = StringVar()
    result_str.set('                                ')
    result.config(textvariable=result_str, relief='flat')
    can.create_window(0,400, anchor="nw", window=result)

	# Lancer le programme
    win.mainloop()

if __name__=="__main__":
    run_radio()