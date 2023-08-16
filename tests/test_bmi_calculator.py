from utils.utils import calculate_bmi_value
import numpy as np
import pytest

def test_valid_imput_bmi_calculation()-> None:
    weight = 100
    height = 165

    assert  calculate_bmi_value(weight=weight, height=height) == 36.73

def test_missing_input_bmi_calculation()-> None:
    if np.random.rand() < 0.5:
        weight, height = '', 165
    else:
        weight, height = 100, ''

    with pytest.raises(ValueError):
        calculate_bmi_value(weight=weight, height=height)

def test_incorrect_input_bmi_calculation()-> None:
    if np.random.rand() < 0.5:
        weight, height = 'hundred', 165
    else:
        weight, height = 100, 'eighty five kilos'

    with pytest.raises(ValueError):
        calculate_bmi_value(weight=weight, height=height)


