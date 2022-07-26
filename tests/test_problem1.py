import pytest
from problem_1 import problem1
from problem_1.exceptions import InvalidQuadraticEqParam

complex_solutions_test_data = [
    (5, 3, 2, (complex(-0.30, 0.56), complex(-0.30, -0.56))),
    (65, 26, 269, (complex(-0.20, 2.02), complex(-0.20, -2.02))),
    (-45, 13, -89, (complex(0.14, 1.40), complex(0.14, -1.40))),
    (5, 65, -56, (0.81, -13.81)),
    (45, 156, -5, (0.03, -3.50)),
    (45, 13, -89, (1.27, -1.56)),
    (0, 0, 0, "Quadratic equation has infinitely many solutions."),
    (0, 2, 5, 2.50),
    (5, 0, 5, (complex(0, 1), complex(0, -1))),
    (5, 0, 5, (complex(0, 1), complex(0, -1))),
    (45, 85, 0, (0, -1.89)),
    (1, 1, 1, (complex(-0.50, 0.87), complex(-0.50, -0.87))),
    (-5.2, 6.65, 5.65, (1.86, -0.58)),
]

complex_solutions_exceptions_test_data = [
    ("-5.2", 6.65, 5.65, (1.86, -0.58)),
    (-5.2, "6.65", 5.65, (1.86, -0.58)),
    (-5.2, 6.65, "5.65", (1.86, -0.58)),
]


@pytest.mark.parametrize("a, b, c, expected", complex_solutions_test_data)
def test_quadratic_equation(a, b, c, expected):
    result = problem1.quadratic_equation(a, b, c)
    assert result == expected or result == tuple(reversed(expected))


@pytest.mark.parametrize("a, b, c, expected", complex_solutions_exceptions_test_data)
def test_quadratic_equation_exception(a, b, c, expected):
    try:
        result = problem1.quadratic_equation(a, b, c)
        assert result == expected or result == tuple(reversed(expected))
    except InvalidQuadraticEqParam as e:
        assert type(e) == InvalidQuadraticEqParam
