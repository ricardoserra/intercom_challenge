from pytest import approx, raises

from src.distance import distance_between_points

# floating Point tolerance to be used in unit tests
FLOATING_POINT_TOLERANCE = 0.001


def test_distance_between_tower_brigde_and_eiffel_tower():
    tower_bridge = (51.503378, -0.076579)
    eiffel_tower = (48.8583, 2.294499999999971)
    distance = distance_between_points(
        tower_bridge[0], tower_bridge[1], eiffel_tower[0], eiffel_tower[1])
    assert distance == approx(339.089, rel=FLOATING_POINT_TOLERANCE)


def test_distance_between_dublin_office_temple_bar():
    dublin_office = (53.339428, -6.257664)
    temple_bar = (53.345602, -6.262875)
    distance = distance_between_points(
        dublin_office[0], dublin_office[1],
        temple_bar[0], temple_bar[1])
    assert distance == approx(0.768, rel=FLOATING_POINT_TOLERANCE)


def test_distance_between_dublin_office_temple_bar_using_strings():
    dublin_office = ("53.339428", "-6.257664")
    temple_bar = ("53.345602", "-6.262875")
    distance = distance_between_points(
        dublin_office[0], dublin_office[1],
        temple_bar[0], temple_bar[1])
    assert distance == approx(0.768, rel=FLOATING_POINT_TOLERANCE)


def test_distance_between_same_location():
    random_location = (51.12233, 0.881233)
    distance = distance_between_points(
        random_location[0], random_location[1],
        random_location[0], random_location[1])
    assert distance == approx(0.000, rel=FLOATING_POINT_TOLERANCE)


def test_distance_using_lists():
    random_location = ([51.12233], [0.881233])
    with raises(TypeError):
        assert distance_between_points(
            random_location[0], random_location[1],
            random_location[0], random_location[1])
