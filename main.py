import math


def calcul(unit, name_triangle, right_angle, length_side1, length_side2):

    all_sides = findSide(name_triangle, right_angle)

    hypothenuse = all_sides[0]

    sideTriangle1 = ''.join(list(all_sides[1]))
    sideTriangle2 = ''.join(list(all_sides[2]))

    side1_length_squared = int(length_side1) ** 2
    side2_length_squared = int(length_side2) ** 2

    result = f"le triangle {name_triangle} est rectangle en {right_angle} d'hypothenuse [{hypothenuse}]\n" \
             f"d'après le théoreme de Pythagore:\n" \
             f"{hypothenuse}² = {sideTriangle1}² + {sideTriangle2}²\n" \
             f"{hypothenuse}² = {length_side1}² + {length_side2}²\n" \
             f"{hypothenuse}² = {side1_length_squared} + {side2_length_squared}\n" \
             f"{hypothenuse}² = {side1_length_squared + side2_length_squared}\n" \
             f"{hypothenuse}² = √{side1_length_squared + side2_length_squared}\n" \
             f"{hypothenuse} = {math.sqrt(side1_length_squared + side2_length_squared)}\n" \
             f"{hypothenuse} = {math.floor(math.sqrt(side1_length_squared + side2_length_squared))}\n\n" \
             f"L'Hypothénuse mesure {math.floor(math.sqrt(side1_length_squared + side2_length_squared))} {unit}"

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
    pass


