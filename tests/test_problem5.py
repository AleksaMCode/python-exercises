import pytest
import sys
from io import StringIO
from problem_5 import problem5

type_error_data = [5.05, "5", '5', (5, 56)]


@pytest.mark.parametrize("print_value, size",
                         [("\n****\n*  *\n****", 4),
                          ("\n***\n***", 3),
                          ])
def test_rectangle_print(print_value: str, size: int):
    captures_stdout = StringIO()  # Creates StringIO object
    sys.stdout = captures_stdout  # Redirects stdout

    problem5.rectangle_draw(size, '*')
    sys.stdout = sys.__stdout__  # Reset redirect

    assert captures_stdout.getvalue() == print_value


@pytest.mark.parametrize("print_value, size",
                         [("\n****\n*  *\n*  *\n****", 4),
                          ("\n**\n**", 2),
                          ])
def test_square_print(print_value: str, size: int):
    captures_stdout = StringIO()  # Creates StringIO object
    sys.stdout = captures_stdout  # Redirects stdout

    problem5.square_draw(size, '*')
    sys.stdout = sys.__stdout__  # Reset redirect

    assert captures_stdout.getvalue() == print_value


@pytest.mark.parametrize("size", type_error_data)
def test_rectangle_draw_type_error(size):
    with pytest.raises(TypeError):
        assert problem5.rectangle_draw(size)


@pytest.mark.parametrize("size", type_error_data)
def test_square_draw_type_error(size):
    with pytest.raises(TypeError):
        assert problem5.square_draw(size)


def test_pattern_size():
    assert problem5.square_draw(1) is False and problem5.rectangle_draw(2) is False
