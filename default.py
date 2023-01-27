import os, string, random, shutil, base64, time

#Générer une chaîne de caractères aléatoires de longueur 4
def rand_str():
    abc = string.ascii_lowercase
    return ''.join(random.choice(abc) for _ in range(4))

def init():
		# Enregistrer l'heure (timestamp) de lancement dans le fichier time
    with open('data/time', "w") as f:
        f.write(str(time.time()))

		# Générer 30 faux dossier dans files et y copier des fichiers corrompus 
    path = "files"
    secret = base64.b64decode("c2toaQ==").decode("utf-8")
    for _ in range(30):
        name = rand_str()
        if name == secret: # Ne pas créer le dossier s'il correspond au nom du vrai
            pass
        os.mkdir(path+"/%s" % (name))
        shutil.copy("data/impots_corrupted.pdf", path+"/%s/impots.pdf" % (name))
    
		# Créer le vrai dossier et y coller le vrai fichier
    os.mkdir(path+"/%s" % (secret))
    shutil.copy("data/impots.pdf", path+"/%s/impots.pdf" % (secret))

		# Enregistrer dans generated que les fichiers ont été générés
    with open("data/generated", "w") as f:
        f.write("True")

# Exécuter uniquement si il n'a pas encore généré les fichiers nécessaires
with open("data/generated") as f:
    if f.read() == "False":
        init()
