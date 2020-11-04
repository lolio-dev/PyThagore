from tkinter import *
from main import calcul, calcHypo

root = Tk()
root.geometry("500x300")


def calculer():
    hypothenuse = calcHypo(sideTriangle1Entry.get(), sideTriangle2Entry.get(), rightAngleEntry.get())
    print(hypothenuse)


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

sideTriangle1Label = Label(root, text="entrer le nom d'un des coté de l'angle droit")
sideTriangle1Label.grid(column=0, row=4)

sideTriangle1Entry = Entry(root)
sideTriangle1Entry.grid(column=1, row=4)

sideTriangle2Label = Label(root, text="entrer le nom du deuxieme coté de l'angle droit")
sideTriangle2Label.grid(column=0, row=5)

sideTriangle2Entry = Entry(root)
sideTriangle2Entry.grid(column=1, row=5)

btnTest = Button(text="test", command=calculer)
btnTest.grid(column=0, row=6)

root.mainloop()
