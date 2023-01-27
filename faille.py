from tkinter import *
# Valeur à Trouver
secret = 152.4

# Execute la commande entrée
def run():
    output.configure(text=eval(entry.get()))

# Lance la fenêtre faille
def run_faille():
    global entry, output
		
	# Créer la fenêtre
    win = Toplevel(bg="black")
    win.title("Faille")
    
	# Titre
    Label(win, text="Le programme suivant Possède une faille de sécurité", bg="black", fg="white").pack()

	# Image
    photo = PhotoImage(file="img/faille.png")
    Label(win, image=photo, bg="black", fg="white").pack()

	# Question
    Label(win, text="Affichez la valeur de : secret", bg="black", fg="white").pack()

	# Sortie
    output = Label(win, text="", bg="black", fg="white")

	# Entrée
    entry = Entry(win, fg="white", bg="black")
    entry.pack()
		
	# Bouton lancer
    Button(win, text="Exécuter", command=run, bg="black", fg="white").pack()

	# Afficher la sortie
    output.pack()

	# Lancer la fenêtre
    win.mainloop()

if __name__ == "__main__":
    run_faille()