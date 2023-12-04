from pytest import mark
from dataclasses import asdict

from day4.solution import ScratchCard


example_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

example_part1_point_values = [8, 2, 2, 1, 0, 0]
example_part2_win_counts = [4, 2, 2, 1, 0, 0]

@mark.parametrize("data_line, expected", [
    [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    {
        'card_number': 1,
        'winning_numbers': [41, 48, 83, 86, 17],
        'play_numbers': [83, 86,  6, 31, 17,  9, 48, 53],
    }
    ],
    [
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    {
        'card_number': 2,
        'winning_numbers': [13, 32, 20, 16, 61],
        'play_numbers': [61, 30, 68, 82, 17, 32, 24, 19],
    }
    ],
    [
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    {
        'card_number': 3,
        'winning_numbers': [1, 21, 53, 59, 44],
        'play_numbers': [69, 82, 63, 72, 16, 21, 14, 1],
    }
    ],
    [
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    {
        'card_number': 4,
        'winning_numbers': [41, 92, 73, 84, 69],
        'play_numbers': [59, 84, 76, 51, 58, 5, 54, 83],
    }
    ],
    [
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    {
        'card_number': 5,
        'winning_numbers': [87, 83, 26, 28, 32],
        'play_numbers': [88, 30, 70, 12, 93, 22, 82, 36],
    }
    ],
    [
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    {
        'card_number': 6,
        'winning_numbers': [31, 18, 13, 56, 72],
        'play_numbers': [74, 77, 10, 23, 35, 67, 36, 11],
    }
    ]
    ]
    )
def test_parse_data_line(data_line, expected):
    test_obj = ScratchCard.from_data_line(data_line)
    assert asdict(test_obj) == expected

@mark.parametrize("data_line, expected_score", zip(example_input.split("\n")[1:-1], example_part1_point_values))
def test_part1_scoring(data_line, expected_score):
    test_obj = ScratchCard.from_data_line(data_line)
    assert test_obj.part1_points == expected_score

@mark.parametrize("data_line, expected_count", zip(example_input.split("\n")[1:-1], example_part2_win_counts))
def test_part2_win_count(data_line, expected_count):
    test_obj = ScratchCard.from_data_line(data_line)
    assert test_obj.win_count == expected_count