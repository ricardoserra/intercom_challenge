from pytest import approx

from src.distance import degrees_to_radians

# Floating Point tolerance to be used in unit tests
FLOATING_POINT_TOLERANCE = 0.001


def test_100_degree_to_radians():
    assert degrees_to_radians(100) == approx(1.745, rel=FLOATING_POINT_TOLERANCE)


def test_2_degree_to_radians():
    assert degrees_to_radians(2) == approx(0.0349, rel=FLOATING_POINT_TOLERANCE)


def test_180_degree_to_radians():
    assert degrees_to_radians(180) == approx(3.141, rel=FLOATING_POINT_TOLERANCE)


def test_minus_180_degree_to_radians():
    assert degrees_to_radians(-180) == approx(-3.141, rel=FLOATING_POINT_TOLERANCE)
