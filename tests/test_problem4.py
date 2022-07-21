import pytest

from problem_4 import problem4


@pytest.mark.parametrize("first_string, second_string, result",
                         [("Meh", "Meh", 0),
                          ("Dum spiro spero", "Iacta alea est", -1),
                          ("Dum spiro spero", "dum spiro spero", 1),
                          ("Iacta alea est", "Iacta alea estt", 1),
                          ])
def test_strcmp(first_string, second_string, result):
    assert problem4.strcmp(first_string, second_string) is result


@pytest.mark.parametrize("first_string, second_string, result",
                         [(5, 6, 0),
                          (5, 542.2, -1),
                          ])
def test_strcmp_type_error(first_string, second_string, result):
    with pytest.raises(TypeError):
        assert problem4.strcmp(first_string, second_string) is result
