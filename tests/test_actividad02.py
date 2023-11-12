import pytest
from src.actividad02 import fahr2cel

@pytest.mark.parametrize(
    "input_fahr, expected",
    [
        (32,  0),
        (111.99992, 44.4444),
        (1.99994, -16.6667)
        
    ]
)
def test_dividir_params(input_fahr, expected):
    assert fahr2cel(input_fahr) == expected


def test_fahr2cel_floatError():
    with pytest.raises(test_fahr2cel_floatError):
        fahr2cel(111.99992, 44.4444)