import os
from tkinter import *
from PIL import Image, ImageTk
import os
# modules internes
import radio, image_opener, notes, decode, faille, default
from positions import check_click


win= Tk() # Créer une fenêtre tkinter

win.attributes('-fullscreen', True) # La mettre en plein écran

w, h = win.winfo_screenwidth(), win.winfo_screenheight() # Récupérer la résolution de l'écran

# Renvoie les données d'une image et change sa résolution pour qu'elle corresponde à celle de l'écran 
def get_img_widget(src):
    img = Image.open(src).resize((w, h))
    img = ImageTk.PhotoImage(image=img, master=win)
    return img

# Dictionnaire des différents fonds
backgrounds = {
    "black": get_img_widget("img/black.png"), 
    "default": get_img_widget("img/back3.png"),
 }

# Liste des chaines de caractères contenues dans les fichiers txt0, txt1, txt2 qui correspondent aux textes d'introduction
intro_strs = [open("data/txt0", encoding="utf-8").read(),open("data/txt1", encoding="utf-8").read(), open("data/txt2", encoding="utf-8").read()]

# Identifiant de la page actuelle
current_page=0

# Fenêtre correspondant au click sur l'imprimante
def imprimante():
    win2 = Toplevel()
    win2.title("Imprimante")
    Label(win2, text="Il semblerai qu'un fichier contenu dans "+os.path.abspath("files/")+"\nsoit protégé par un mot de passe rendant l'impression impossible...").pack()
    win2.mainloop()


# Fonction gérant le click de la souris sur l'écran
def handle_click(event):
    if current_page!=3: # Quitter la fonction si le joueur n'est pas sur le bureau
        return
		
    x, y = event.x, event.y # Coordonnées du click
    new_win_id = check_click(x,y,w,h) # Voir positions.py > check_click()


    if not new_win_id: # Si le click ne correspond à aucune zone quitter
        return
    
    # Ouvrir les fenêtres correspond à leur zone
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
        image_opener.open_image(new_win_id) # voir image_opener.py

# Changer le fond et le texte affiché à l'écran
def update_image():
    global current_page
    current_page+=1
    if current_page==3: # Quand arrivé sur le bureau détruire le bouton suivant ainsi que le Label qui contient le texte affiché à l'écran
        can.itemconfig(image_container,image=backgrounds["default"])  
        info_text.destroy()
        next_button.destroy()
    else:
        info_text.config(text=intro_strs[current_page])


# Canvas qui contient tous les widgets de l'écran
can = Canvas(win, highlightthickness=0)
can.pack(fill='both', expand=1)

# Image contenant le fond
image_container = can.create_image(0,0, anchor="nw",image=backgrounds["black"])

# Définir la fonction associé au click gauche de la souris
can.bind("<Button-1>", handle_click)

# Bouton  de fermeture du jeu 
close_button = Button(can, text="Quitter le jeu", bg="black", fg="red", command=win.destroy, highlightthickness=0, font='Helvetica 18 bold')
close_button.pack(side=BOTTOM)

# Bouton pour passer à l'étape suivante de l'introduction
next_button = Button(can, text="Suivant", bg="black", fg="white", command=update_image)
next_button.pack(side=BOTTOM)

# Texte d'introduction
info_text = Label(can, text = intro_strs[0], fg="white", bg="black", justify=LEFT, font=("Helvetica",30))
info_text.pack(side=BOTTOM)

#Lancer le jeu
win.mainloop()