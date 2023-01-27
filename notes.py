import hashlib
from tkinter import *
import requests, time
keys = [
    "Prénom", 
    "Nom", 
    "Société", 
    "Domicile", 
    "Ville",
    "Code Postal", 
    "Amante\n(prénom)",
    "Arme", 
    "Coordonnées GPS" # https://pastebin.com/Ws7EBrWz
    ]
default = []

new = []
def run_notes():
    global default, win, entries, result

    with open('data/notes') as f:
        default = f.read().split('\n')

    if len(default) < len(keys):
        default = ["" for _ in range(len(keys))]

    win = Toplevel(bg="black")
    win.title("Notes")

    entries = []
    for i in range(len(keys)):
        Label(win, text=keys[i], fg="white", bg="black").grid(row=i)
        entry = Entry(win, fg="white", bg="black")
        entry.insert(0, default[i])
        entries.append(entry)
        entries[i].grid(row=i, column=1)

    Button(win, text="Sauvegarder", command=save, fg="white", bg="black").grid(column=1)
    Button(win, text="Envoyer", command=send, fg="white", bg="black").grid(column=1)
    result = Label(win, fg="white", bg="black")
    result.grid(column=1)
    win.mainloop()

def save():
    global new

    for e in entries:
        new.append(e.get())
    final_str = "\n".join(new)
    with open('data/notes', 'w') as f:
        f.write(final_str)
    new=[]
    win.destroy()

def send():
    global new 
    for e in entries:
        new.append(e.get().replace(' ','').upper())
    print(hashlib.md5(str(new).encode("utf-8")).hexdigest())
    url = "https://investigatethedesk.000webhostapp.com/index.php?hex="+hashlib.md5(str(new).encode("utf-8")).hexdigest()
    new=[]
    response = requests.get(url=url)
    status_code = response.status_code
    if status_code != 200:
        result.configure(text="Erreur de connexion verifiez votre connexion internet")
        return
    
    response = response.content.decode("utf-8")
    print(response)
    if response == "False":
        result.configure(text="Vous semblez vous être trompé sur un des éléments...")
        return
    
    with open("data/time", "r") as f:
        timestamp_start = float(f.read())
        timestamp_end = time.time()
        diff_min = (timestamp_end - timestamp_start) // 60

        result.configure(text=response+str(diff_min)+" minutes")
    

if __name__ == "__main__":
    run_notes()