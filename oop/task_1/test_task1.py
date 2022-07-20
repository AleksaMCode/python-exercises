import pytest
import task1

test_complex_solutions = [
    (5, 3, 2, (complex(-0.3, 0.56), complex(-0.3, -0.56))),
    (65, 26, 269, (complex(-0.2, 2.02), complex(-0.2, -2.02))),
    (-45, 13, -89, (complex(0.14, 1.39), complex(-0.2, -1.39))),
]

test_real_solutions = [
    (5, 65, -56, 0.81, -13.81),
    (45, 156, -5, 0.03, -3.49),
    (45, 13, -89, 1.27, -1.56),
]


@pytest.mark.parametrize("a,b,expected", test_complex_solutions)
def test_quadratic_equation(a, b, c, expected):
    assert task1.quadratic_equation(5, 3, 2) == expected
