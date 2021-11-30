import pytest
from morse import encode, decode


@pytest.mark.parametrize('morse_message, exp', [
    ('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.', 'MAI-PYTHON-2019'),
    ('.- -.-. .- -.. . -- -.-- -....- ..--- ----- ..--- .----', 'ACADEMY-2021'),
    ('... --- ...', 'SOS')
])
def test_decode(morse_message, exp):
    assert decode(morse_message) == exp


@pytest.mark.parametrize('message, exp', [
    ('MAI-PYTHON-2019', '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'),
    ('ACADEMY-2021', '.- -.-. .- -.. . -- -.-- -....- ..--- ----- ..--- .----'),
    ('SOS', '... --- ...')
])
def test_encode(message, exp):
    assert encode(message) == exp
