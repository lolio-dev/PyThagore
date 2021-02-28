import math


def calcul(unit: str, name_triangle: str, right_angle: str, length_side1: int, length_side2: int):
    """
    :param unit: unité du triangle
    :param name_triangle: nom du triangle
    :param right_angle: angle droit du triangle
    :param length_side1: longueur du premier côté de l'angle droit du triangle
    :param length_side2: longueur du deuxieme côté de l'angle droit du triangle
    :return: calcul du théoreme de pythagore rédigé
    """

    all_sides = find_side(name_triangle, right_angle)

    hypothenuse = all_sides[0]

    side_triangle1 = ''.join(list(all_sides[1]))
    side_triangle2 = ''.join(list(all_sides[2]))

    side1_length_squared = int(length_side1) ** 2
    side2_length_squared = int(length_side2) ** 2

    result = f"le triangle {name_triangle} est rectangle en {right_angle} d'hypothenuse [{hypothenuse}]\n" \
             f"d'après le théoreme de Pythagore:\n" \
             f"{hypothenuse}² = {side_triangle1}² + {side_triangle2}²\n" \
             f"{hypothenuse}² = {length_side1}² + {length_side2}²\n" \
             f"{hypothenuse}² = {side1_length_squared} + {side2_length_squared}\n" \
             f"{hypothenuse}² = {side1_length_squared + side2_length_squared}\n" \
             f"{hypothenuse}² = √{side1_length_squared + side2_length_squared}\n" \
             f"{hypothenuse} = {math.sqrt(side1_length_squared + side2_length_squared)}\n" \
             f"{hypothenuse} = {math.floor(math.sqrt(side1_length_squared + side2_length_squared))}\n\n" \
             f"L'Hypothénuse mesure {math.floor(math.sqrt(side1_length_squared + side2_length_squared))} {unit}"

    return result


def find_side(name_triangle, right_angle):
    triangle = name_triangle
    right_angle = right_angle

    all_angles = [i for i in triangle]
    all_angles.remove(right_angle)

    hypothenuse = "".join(all_angles)

    all_sides = [i for i in name_triangle]
    all_sides.remove(right_angle)
    side1 = all_sides[0], right_angle
    side2 = all_sides[1], right_angle

    return hypothenuse, side1, side2


if __name__ == '__main__':
    print(calcul("cm", "abc", "b", 4, 6))


