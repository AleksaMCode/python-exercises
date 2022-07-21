import math


def quadratic_equation(a, b, c):
    """
    Calculates the solution to the quadratic equation using Vieta's formula.
    :param a: Leading coefficient value in quadratic equation
    :param b: Coefficient of a polynomial variable of degree one
    :param c: Coefficient of a polynomial variable of the lowest degree
    :return: Quadratic equation solution(s) in Tuple form
    """
    discriminant = b * b - 4 * a * c

    if a == b == c == 0:
        return "Quadratic equation has infinitely many solutions."
    elif a == 0:
        return round(c / b, 2)
    elif discriminant < 0:
        discriminant *= -1
        re = round(-b / (2 * a), 2)
        im = round(math.sqrt(discriminant) / (2 * a), 2)
        return complex(re, im), complex(re, -im)
    else:
        return round((-b + math.sqrt(discriminant)) / (2 * a), 2), round((-b - math.sqrt(discriminant)) / (2 * a), 2)
