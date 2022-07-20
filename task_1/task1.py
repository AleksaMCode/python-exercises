import math


def quadratic_equation(a, b, c):
    determinant = b * b - 4 * a * c

    if a == b == c == 0:
        return "Quadratic equation has infinitely many solutions."
    elif a == 0:
        return round(c / b, 2)
    elif determinant < 0:
        determinant *= -1
        re = round(-b / (2 * a), 2)
        im = round(math.sqrt(determinant) / (2 * a), 2)

        im = im if im > 0 else im * -1
        return complex(re, im), complex(re, -im)
    else:
        return round((-b + math.sqrt(determinant)) / (2 * a), 2), round((-b - math.sqrt(determinant)) / (2 * a), 2)
