from tkinter import *
from PIL import Image, ImageTk

def open_image(name):

	# Créer une fenêtre
    win = Toplevel()
    win.title(name)

	# Ouvre l'image
    img = PhotoImage(file="img/%s.png" % name)

	# Récupérer la résolution
    w, h = img.width(), img.height()

	# Afficher image
    img_lab = Label(win)
    img_lab.config(image=img)
    img_lab.pack()

# Définir les dimensions de la fenêtre avec la résolution de l'image
    win.minsize(w,h)
    win.maxsize(w,h)

# Lancer la fenêtre
    win.mainloop()
