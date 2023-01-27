import hashlib
from tkinter import *
import requests, time

# Liste des noms des entrée du formulaire
keys = [
    "Prénom", 
    "Nom", 
    "Société", 
    "Domicile", 
    "Ville",
    "Code Postal", 
    "Amante\n(prénom)",
    "Arme", 
    "Coordonnées GPS"
    ]

# Définir la liste des nouvelles entrées comme vide
new = []
def run_notes():
    global default, win, entries, result

		# Récupérer les données déjà sauvegardées dans data/notes
    with open('data/notes') as f:
        default = f.read().split('\n')

		# Si data/notes n'a pas suffisament de valeurs alors on définit toutes les valeurs comme vides
    if len(default) < len(keys):
        default = ["" for _ in range(len(keys))]

		# Créer une fenêtre nommé Notes
    win = Toplevel(bg="black")
    win.title("Notes")

		# Listes des widgets de type Entry
    entries = []
		
		# Pour chaque nom d'entrée créer une entrée dans entries et un texte content le nom
    for i in range(len(keys)):
        Label(win, text=keys[i], fg="white", bg="black").grid(row=i)
        entry = Entry(win, fg="white", bg="black")
        entry.insert(0, default[i]) # Rentrer la valeur sauvegardée préalablement sinon rien
        entries.append(entry)
        entries[i].grid(row=i, column=1)

		# Boutons sauvegarder appelle la fonction save, envoyer appelle la fonction send
    Button(win, text="Sauvegarder", command=save, fg="white", bg="black").grid(column=1)
    Button(win, text="Envoyer", command=send, fg="white", bg="black").grid(column=1)

		# Champs de texte contenant la réponse de send
    result = Label(win, fg="white", bg="black")
    result.grid(column=1)

    win.mainloop()

# Sauvegarder les entrées dans le fichier data/notes
def save():
    global new

		# Pour chaque entrée ajouter sa valeur à new
    for e in entries:
        new.append(e.get())

		# Transformer le tout en une chaine de caractère contenant une valeur par ligne
    final_str = "\n".join(new)

		# Enregistrer dans data/notes
    with open('data/notes', 'w') as f:
        f.write(final_str)

    win.destroy()

# Envoyer les valeurs au server pour vérifier si elles sont correctes
def send():
    global new 

	# Pour chaque entrée ajouter sa valeur à new
    for e in entries:
        new.append(e.get().replace(' ','').upper()) # Retirer les minuscules et espaces pour limiter les erreurs de frappe

	# Créer le hash correspondant à la liste new
    hash_new = hashlib.md5(str(new).encode("utf-8")).hexdigest()
    url = "https://investigatethedesk.000webhostapp.com/index.php?hex="+hash_new

	# Réinitialiser les valeurs de new
    new=[]

	# Exécuter la requête http get vers le serveur
    response = requests.get(url=url)
    status_code = response.status_code

	# Si le code de la réponse n'est pas 200 alors il y a eu une erreur réseau
    if status_code != 200:
        result.configure(text="Erreur de connexion verifiez votre connexion internet")
        return
    
	# Récupérer le texte de la réponse du serveur
    response = response.content.decode("utf-8")

	# Si le serveur renvoie False alors le hash n'est pas le bon les valeurs rentrées sont fausses
    if response == "False":
        result.configure(text="Vous semblez vous être trompé sur un des éléments...")
        return
    
	# Sinon le joueur a gagné on affiche donc le temps qu'il a mis pour résoudre l'enquête ainsi que la réponse du serveur, une autre énigme ?
    with open("data/time", "r") as f:
        timestamp_start = float(f.read())
        timestamp_end = time.time()
        diff_min = (timestamp_end - timestamp_start) // 60

        result.configure(text=response+" "+str(diff_min)+" minutes")
    

if __name__ == "__main__":
    run_notes()
