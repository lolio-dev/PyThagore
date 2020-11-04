# import des bibliothèques
import math
import sys


def calcul(unit, name_triangle, right_angle, side_triangle2, side_triangle3, length_side2, length_side3):
    units = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

    if not unit in units:
        print("veuillez n'entrer que une unité de longueur valide")
        sys.exit()

    if not length_side2.isdigit() or not length_side3.isdigit():
        print("Vous ne devez entrer que des nombres, pas de lettre ni de caractere speciaux")
        sys.exit()

    hypothenuse = calcHypo("abc", "b")
    side2_length_squared = int(length_side2) ** 2
    side3_length_squared = int(length_side3) ** 2

    result = f"le triangle {name_triangle} est rectangle en {right_angle} d'hypothenuse {hypothenuse}\n" \
             f"d'après le théoreme de phytagore:\n" \
             f"on a: {hypothenuse}² = {side_triangle2}² + {side_triangle3}²\n" \
             f"      {hypothenuse}² = {length_side2}² + {length_side3}²\n" \
             f"      {hypothenuse}² = {side2_length_squared} + {side3_length_squared}\n" \
             f"      {hypothenuse}² = {side2_length_squared + side3_length_squared}\n" \
             f"      {hypothenuse}² = √{side2_length_squared + side3_length_squared}\n" \
             f"      {hypothenuse} = {math.sqrt(side2_length_squared + side3_length_squared)}\n" \
             f"      {hypothenuse} = {math.floor(math.sqrt(side2_length_squared + side3_length_squared))}\n\n" \
             f"      L'ypothénuse mesure {math.floor(math.sqrt(side2_length_squared + side3_length_squared))} {unit}"

    print(result)
    return result


def calcHypo(triangle_name, right_angle):
    triangle = triangle_name
    angleDroit = right_angle

    eachAngle = [i for i in triangle]
    eachAngle.remove(angleDroit)

    hypothenuse = "".join(eachAngle)
    print(hypothenuse)
    return hypothenuse


if __name__ == '__main__':
    calcul("cm", "abc", "b", "ab", "bc", "20", "15")
