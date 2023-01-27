# Liste des emplacements des zones cliquables
positions = [
        ((981, 146), (1348, 370), "ordi"), #Ordi
        ((722, 465), (967, 603), "radio"), #Radio
        ((2278,1248), (2560, 1440), "notes"), #Notes
        ((2278, 1014), (2556, 1248), "decode"), #Decode
        ((621, 653), (866, 734), "poeme"), #Poème
        ((1542, 305), (1641, 401), "phone"), #Phone
        ((1793, 344), (2099, 533), "imprimante"), #Imprimante
        ((1431, 346), (1510, 403), "chocolat"), #Chocolat
        ((415, 609), (674, 669), "faille")

 ]

# Renvoie les coordonnées de la souris traduites comme si elles correspondait à un écran de résolution 2560x2440
def scale(x,y,w,h):
    x = 2560*x//w
    y = 1440*y//h
    return x,y

# Vérifie si le click rentré correspond à une des zones cliquable et si oui renvoie son nom sinon renvoie False
def check_click(x,y,w,h):
    result=False
    x, y = scale(x,y,w,h)
    for i in positions:
        a = i[0]
        b = i[1]
        if (a[0] < x < b[0]) and (a[1] < y < b[1]):
            result = i[2]
            return result
    return False