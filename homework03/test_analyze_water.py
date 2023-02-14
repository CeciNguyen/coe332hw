from water_analyzer import calc_turb, calc_min_time
import pytest

def test_calc_turb():
    turbDict = [1,2,3,4,5]
    a0 = 0.23
    I90 = [0.22, 0.23, 0.24, 0.25, 0.26]
    expected = 0.239
    assert calc_turb(turbDict, a0, I90) == expected

def test_calc_min_time():
    Ts = 1.0
    T = 1.5
    d = 0.02
    expected = 6.67
    assert calc_min_time(6.67) == expected
