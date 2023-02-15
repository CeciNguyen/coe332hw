from water_analyzer import calc_turb, calc_min_time
import pytest

def test_calc_turb():
    turbDict = [{"calibration_constant":0.1, "detector_current":1},
                {"calibration_constant":0.1, "detector_current":2},
                {"calibration_constant":0.1, "detector_current":3},
                {"calibration_constant":0.1, "detector_current":4},
                {"calibration_constant":0.1, "detector_current":5}]
    expected = 0.3
    assert float(calc_turb(turbDict, 'calibration_constant', 'detector_current')) == expected


def test_calc_turb():
    turbDict = [{"calibration_constant":0.23, "detector_current":0.22},
                {"calibration_constant":0.23, "detector_current":0.23},
                {"calibration_constant":0.23, "detector_current":0.24},
                {"calibration_constant":0.23, "detector_current":0.25},
                {"calibration_constant":0.23, "detector_current":0.26}]
    expected = 0.0552
    assert float(calc_turb(turbDict, 'calibration_constant', 'detector_current')) == expected


def test_calc_min_time():
    currTurb = 3
    expected = 100
    assert calc_min_time(currTurb) == expected

def test_calc_min_time():
    currTurb = 6.2
    expected = 260
    assert calc_min_time(currTurb) == expected
