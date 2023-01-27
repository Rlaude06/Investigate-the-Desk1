import os, string, random, shutil, base64, time


def rand_str():
    """Générer une chaîne aléatoire de longueur fixe"""
    abc = string.ascii_lowercase
    return ''.join(random.choice(abc) for _ in range(4))

def init():
    with open('data/time', "w") as f:
        f.write(str(time.time()))

    path = "files"
    secret = base64.b64decode("c2toaQ==").decode("utf-8")
    for _ in range(30):
        name = rand_str()
        if name == secret:
            pass
        os.mkdir(path+"/%s" % (name))
        shutil.copy("data/impots_corrupted.pdf", path+"/%s/impots.pdf" % (name))
    
    os.mkdir(path+"/%s" % (secret))
    shutil.copy("data/impots.pdf", path+"/%s/impots.pdf" % (secret))
    with open("data/generated", "w") as f:
        f.write("True")

with open("data/generated") as f:
    if f.read() == "False":
        init()