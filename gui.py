from tkinter import *
from main import calcul

root = Tk()
root.geometry("500x300")


def calculer():
	print("hello world")


unitLabel = Label(root, text="entrer l'unité des longueur du triangle rectangle: ")
unitLabel.grid(column=0, row=1)

unitEntry = Entry(root)
unitEntry.grid(column=1, row=1)

nameLabel = Label(root, text="Entrer le nom du triangle rectangle: ")
nameLabel.grid(column=0, row=2)

nameEntry = Entry(root)
nameEntry.grid(column=1, row=2)

rightAngleLabel = Label(root, text="Entrer le nom de l'angle droit: ")
rightAngleLabel.grid(column=0, row=3)

rightAngleEntry = Entry(root)
rightAngleEntry.grid(column=1, row=3)

calculBtn = Button(root, text="calculer", command=calculer)
calculBtn.grid(column=0, row=4)
root.mainloop()
