from mlproject.distance import haversine


def test_type_of_haversine():
    assert type(haversine(45.453, 34.3455, 23.3423, 1.234)) == float
