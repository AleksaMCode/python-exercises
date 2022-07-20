import math


def quadratic_equation(a, b, c):
    determinant = b * b - 4 * a * c
    if determinant < 0:
        determinant *= -1
        re = round(-b / (2 * a), 2)
        im = round(math.sqrt(determinant) / (2 * a), 2)
        print("Solution is: %.2f +/- %.2fi" % (re, im))
        return complex(re, im), complex(re, -im)
    else:
        return round((-b + math.sqrt(determinant)) / (2 * a), 2), round((-b - math.sqrt(determinant)) / (2 * a), 2)
        # print("Solution is: %.2f or %.2f" % (
        #     (-b + math.sqrt(determinant)) / (2 * a), (-b - math.sqrt(determinant)) / (2 * a)))
