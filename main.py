# import des bibliothèques
import math
import sys


def calcul(unit, name_triangle, right_angle, side_triangle2, side_triangle3, hypothenuse, length_side2, length_side3):
    units = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

    if not unit in units:
        print("veuillez n'entrer que une unité de longueur valide")
        sys.exit()

    if not length_side2.isdigit() or not length_side3.isdigit():
        print("Vous ne devez entrer que des nombres, pas de lettre ni de caractere speciaux")
        sys.exit()

    print(f"le triangle {name_triangle} est rectangle en {right_angle} d'hypothenuse {hypothenuse}")
    print("déprès le théoreme de phytagore:")
    print(f"on a: {hypothenuse}² = {side_triangle2}² + {side_triangle3}²")
    print(f"      {hypothenuse}² = {length_side2}² + {length_side3}²")

    side2_length_squared = int(length_side2) ** 2
    side3_length_squared = int(length_side3) ** 2

    print(f"      {hypothenuse}² = {side2_length_squared} + {side3_length_squared}")
    print(f"      {hypothenuse}² = {side2_length_squared + side3_length_squared}")
    print(f"      {hypothenuse}² = √{side2_length_squared + side3_length_squared}")
    print(f"      {hypothenuse} = {math.sqrt(side2_length_squared + side3_length_squared)}")
    print(f"      {hypothenuse} = {math.floor(math.sqrt(side2_length_squared + side3_length_squared))}")

    print(f"      L'ypothénuse mesure {math.floor(math.sqrt(side2_length_squared + side3_length_squared))} {unit}")


if __name__ == '__main__':
    unit = input("entrer l'unité des longueur du triangle")
    name_triangle = input("entrer le nom du triangle")  # nom du triangle

    right_angle = input("entrer le sommet de l'angle droit")  # sommet de l'angle droit

    side_triangle2 = input("entrer le nom du coté 1")
    side_triangle3 = input("entrer le nom du coté 2")

    hypothenuse = input("entrer la nom du coté de l'hypothenuse")

    length_side2 = input("entrer la longueur du 2eme coté")
    length_side3 = input("entrer la longueur du 3eme coté")

    calcul(unit, name_triangle, right_angle, side_triangle2, side_triangle3, hypothenuse, length_side2, length_side3)

