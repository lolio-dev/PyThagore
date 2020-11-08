# import des bibliothèques
import math
import sys


def calcul(unit, name_triangle, right_angle, length_side1, length_side2):
    units = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

    if not unit in units:
        print("veuillez n'entrer que une unité de longueur valide")
        sys.exit()

    if not length_side1.isdigit() or not length_side2.isdigit():
        print("Vous ne devez entrer que des nombres, pas de lettre ni de caractere speciaux")
        sys.exit()

    all_sides = findSide(name_triangle, right_angle)

    hypothenuse = all_sides[0]

    sideTriangle1 = ''.join(list(all_sides[1]))
    sideTriangle2 = ''.join(list(all_sides[2]))

    side1_length_squared = int(length_side1) ** 2
    side2_length_squared = int(length_side2) ** 2

    result = f"le triangle {name_triangle} est rectangle en {right_angle} d'hypothenuse [{hypothenuse}]\n" \
             f"d'après le théoreme de phytagore:\n" \
             f"" \
             f"{hypothenuse}² = {sideTriangle1}² + {sideTriangle2}²\n" \
             f"{hypothenuse}² = {length_side1}² + {length_side2}²\n" \
             f"{hypothenuse}² = {side1_length_squared} + {side2_length_squared}\n" \
             f"{hypothenuse}² = {side1_length_squared + side2_length_squared}\n" \
             f"{hypothenuse}² = √{side1_length_squared + side2_length_squared}\n" \
             f"{hypothenuse} = {math.sqrt(side1_length_squared + side2_length_squared)}\n" \
             f"{hypothenuse} = {math.floor(math.sqrt(side1_length_squared + side2_length_squared))}\n\n" \
             f"L'ypothénuse mesure {math.floor(math.sqrt(side1_length_squared + side2_length_squared))} {unit}"

    return result


def findSide(name_triangle, right_angle):
    triangle = name_triangle
    angleDroit = right_angle

    eachAngle = [i for i in triangle]
    eachAngle.remove(angleDroit)

    hypothenuse = "".join(eachAngle)

    allSides = [i for i in name_triangle]
    allSides.remove(right_angle)
    side1 = allSides[0], right_angle
    side2 = allSides[1], right_angle

    return hypothenuse, side1, side2


if __name__ == '__main__':
    print(calcul("cm", "abc", "b", "15", "17"))


