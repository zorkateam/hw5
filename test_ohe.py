import pytest
from one_hot_encoder import fit_transform


@pytest.mark.parametrize('cities, exp', [
    (['Moscow', 'New York', 'Moscow', 'London'], [('Moscow', [0, 0, 1]),
                                                  ('New York', [0, 1, 0]),
                                                  ('Moscow', [0, 0, 1]),
                                                  ('London', [1, 0, 0])]),
    (['Moscow'], [('Moscow', [1])]),
    (['London', 'Paris'], [('London', [0, 1]),
                           ('Paris', [1, 0])]),
    ([], [])
])
def test_ft(cities, exp):
    assert fit_transform(cities) == exp


def test_exception():
    with pytest.raises(TypeError):
        fit_transform(1)
