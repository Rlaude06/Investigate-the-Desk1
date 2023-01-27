from tkinter import *
secret = 152.4

def run():
    output.configure(text=eval(entry.get()))

def run_faille():
    global entry, output
    win = Toplevel(bg="black")
    win.title("Faille")
    
    Label(win, text="Le programme suivant Possède une faille de sécurité", bg="black", fg="white").pack()

    photo = PhotoImage(file="img/faille.png")
    Label(win, image=photo, bg="black", fg="white").pack()

    Label(win, text="Affichez la valeur de : secret", bg="black", fg="white").pack()

    output = Label(win, text="", bg="black", fg="white")


    entry = Entry(win, fg="white", bg="black")
    entry.pack()
    Button(win, text="Exécuter", command=run, bg="black", fg="white").pack()
    output.pack()
    win.mainloop()

if __name__ == "__main__":
    run_faille()