from day9.solution import generate_difference_list, generate_prediction_pyramid, generate_prediction, generate_backward_prediction
from pytest import mark


@mark.parametrize("input, expected", [
    [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3]],
    [[3, 3, 3, 3, 3], [0,0,0,0]],
])
def test_generate_difference_list(input, expected):
    assert generate_difference_list(input) == expected

@mark.parametrize("input, expected", [
    [[0, 3, 6, 9, 12, 15], [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0,0,0,0]]],
    [[10, 13, 16, 21, 30, 45], [[10, 13, 16, 21, 30, 45], [3, 3, 5, 9, 15], [0, 2, 4, 6], [2, 2, 2], [0, 0]]],
])
def test_generate_prediction_pyramid(input, expected):
    assert generate_prediction_pyramid(input) == expected

@mark.parametrize("input, expected", [
    [[[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0,0,0,0]], 18],
    [[[10, 13, 16, 21, 30, 45], [3, 3, 5, 9, 15], [0, 2, 4, 6], [2, 2, 2], [0, 0]], 68],
])
def test_generate_prediction(input, expected):
    assert generate_prediction(input) == expected

@mark.parametrize("input, expected", [
    [[[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0,0,0,0]], -3],
    [[[10, 13, 16, 21, 30, 45], [3, 3, 5, 9, 15], [0, 2, 4, 6], [2, 2, 2], [0, 0]], 5],
])
def test_generate_backward_prediction(input, expected):
    assert generate_backward_prediction(input) == expected