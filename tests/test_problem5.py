import pytest

from problem_5 import problem5

type_error_data = [5.05, "5", '5', (5, 56)]


@pytest.mark.parametrize("size", type_error_data)
def test_rectangle_draw_type_error(size):
    with pytest.raises(TypeError):
        assert problem5.rectangle_draw(size)


@pytest.mark.parametrize("size", type_error_data)
def test_square_draw_type_error(size):
    with pytest.raises(TypeError):
        assert problem5.square_draw(size)
