from pytest import mark

from day6.solution import calculate_distance, find_minmax_winner

@mark.parametrize('hold_time, total_time, expected_distance', [
    [0,7,0],
    [1,7,6],
    [2,7,10],
    [3,7,12],
    [4,7,12],
    [5,7,10],
    [6,7,6],
    [7,7,0]
    ])
def test_calculate_distance(hold_time, total_time, expected_distance):
    assert calculate_distance(hold_time, total_time) == expected_distance

@mark.parametrize('total_time, winning_distance, min, expected_value', [
    [7,9,True,2],
    [15,40,True,4],
    [30,200,True,11],
    [7,9,False,5],
    [15,40,False,11],
    [30,200,False,19],
    [48,261,True,7]
])
def test_find_minmax_winner(total_time, winning_distance, min, expected_value):
    assert find_minmax_winner(total_time, winning_distance, min) == expected_value    