from tkinter import *
from main import calcul

root = Tk()
root.geometry("520x350")


def calculer():
    result = calcul(unitEntry.get(), nameEntry.get(), rightAngleEntry.get(), side1Entry.get(), side2Entry.get())
    resultLabel.config(text=result)


unitLabel = Label(root, text="entrer l'unité des longueur du triangle rectangle: ")
unitLabel.grid(column=0, row=1)

unitEntry = Entry(root)
unitEntry.grid(column=1, row=1)

nameLabel = Label(root, text="Entrer le nom du triangle rectangle: ")
nameLabel.grid(column=0, row=2)

nameEntry = Entry(root)
nameEntry.grid(column=1, row=2)

rightAngleLabel = Label(root, text="Entrer le nom du sommet de l'angle droit: ")
rightAngleLabel.grid(column=0, row=3)

rightAngleEntry = Entry(root)
rightAngleEntry.grid(column=1, row=3)

side1Label = Label(root, text="Entrer la longueur du premier coté de langle droit: ")
side1Label.grid(column=0, row=4)

side1Entry = Entry(root)
side1Entry.grid(column=1, row=4)

side2Label = Label(root, text="Entrer la longueur du deuxieme coté de langle droit: ")
side2Label.grid(column=0, row=5)

side2Entry = Entry(root)
side2Entry.grid(column=1, row=5)


btnCalculer = Button(text="calculer", command=calculer)
btnCalculer.grid(column=0, row=6, pady=20)

resultLabel = Label(root, text="")
resultLabel.grid(column=0, row=7)

root.mainloop()
