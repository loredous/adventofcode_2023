from day2.solution import split_line, is_game_possible, get_game_power
from pytest import mark


@mark.parametrize(
    "line, expected",
    [
        [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            {
                "number": 1,
                "rounds": [
                    [(3, "blue"), (4, "red")],
                    [(1, "red"), (2, "green"), (6, "blue")],
                    [(2, "green")],
                ],
                "totals": {"red": 5, "green": 4, "blue": 9},
                "maximums": {"red": 4, "green": 2, "blue": 6},
            },
        ],
        [
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            {
                "number": 2,
                "rounds": [
                    [(1, "blue"), (2, "green")],
                    [(3, "green"), (4, "blue"), (1, "red")],
                    [(1, "green"), (1, "blue")],
                ],
                "totals": {"red": 1, "green": 6, "blue": 6},
                "maximums": {"red": 1, "green": 3, "blue": 4},
            },
        ],
        [
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            {
                "number": 3,
                "rounds": [
                    [(8, "green"), (6, "blue"), (20, "red")],
                    [(5, "blue"), (4, "red"), (13, "green")],
                    [(5, "green"), (1, "red")],
                ],
                "totals": {"red": 25, "green": 26, "blue": 11},
                "maximums": {"red": 20, "green": 13, "blue": 6},
            },
        ],
        [
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            {
                "number": 4,
                "rounds": [
                    [(1, "green"), (3, "red"), (6, "blue")],
                    [(3, "green"), (6, "red")],
                    [(3, "green"), (15, "blue"), (14, "red")],
                ],
                "totals": {"red": 23, "green": 7, "blue": 21},
                "maximums": {"red": 14, "green": 3, "blue": 15},
            },
        ],
        [
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
            {
                "number": 5,
                "rounds": [
                    [(6, "red"), (1, "blue"), (3, "green")],
                    [(2, "blue"), (1, "red"), (2, "green")],
                ],
                "totals": {"red": 7, "green": 5, "blue": 3},
                "maximums": {"red": 6, "green": 3, "blue": 2},
            },
        ],
    ],
)
def test_split_line(line, expected):
    assert split_line(line) == expected


@mark.parametrize("game, rgb_max, expected",
    [
        [
            {
                "number": 1,
                "rounds": [
                    [(3, "blue"), (4, "red")],
                    [(1, "red"), (2, "green"), (6, "blue")],
                    [(2, "green")],
                ],
                "totals": {"red": 5, "green": 4, "blue": 9},
                "maximums": {"red": 4, "green": 2, "blue": 6},
            },
            (12, 13, 14),
            True,
        ],
        [
            {
                "number": 2,
                "rounds": [
                    [(1, "blue"), (2, "green")],
                    [(3, "green"), (4, "blue"), (1, "red")],
                    [(1, "green"), (1, "blue")],
                ],
                "totals": {"red": 1, "green": 6, "blue": 6},
                "maximums": {"red": 1, "green": 3, "blue": 4},
            },
            (12, 13, 14),
            True,
        ],
        [
            {
                "number": 3,
                "rounds": [
                    [(8, "green"), (6, "blue"), (20, "red")],
                    [(5, "blue"), (4, "red"), (13, "green")],
                    [(5, "green"), (1, "red")],
                ],
                "totals": {"red": 25, "green": 26, "blue": 11},
                "maximums": {"red": 20, "green": 13, "blue": 6},
            },
            (12, 13, 14),
            False
        ],
        [
            {
                "number": 4,
                "rounds": [
                    [(1, "green"), (3, "red"), (6, "blue")],
                    [(3, "green"), (6, "red")],
                    [(3, "green"), (15, "blue"), (14, "red")],
                ],
                "totals": {"red": 23, "green": 7, "blue": 21},
                "maximums": {"red": 14, "green": 3, "blue": 15},
            },
            (12, 13, 14),
            False
        ],
        [
            {
                "number": 5,
                "rounds": [
                    [(6, "red"), (1, "blue"), (3, "green")],
                    [(2, "blue"), (1, "red"), (2, "green")],
                ],
                "totals": {"red": 7, "green": 5, "blue": 3},
                "maximums": {"red": 6, "green": 3, "blue": 2},
            },
            (12, 13, 14),
            True
        ]
    ])
def test_is_game_possible(game, rgb_max, expected):
    assert is_game_possible(game, *rgb_max) == expected

@mark.parametrize("game, expected_power",
    [
        [
            {
                "number": 1,
                "rounds": [
                    [(3, "blue"), (4, "red")],
                    [(1, "red"), (2, "green"), (6, "blue")],
                    [(2, "green")],
                ],
                "totals": {"red": 5, "green": 4, "blue": 9},
                "maximums": {"red": 4, "green": 2, "blue": 6},
            },
            48
        ],
        [
            {
                "number": 2,
                "rounds": [
                    [(1, "blue"), (2, "green")],
                    [(3, "green"), (4, "blue"), (1, "red")],
                    [(1, "green"), (1, "blue")],
                ],
                "totals": {"red": 1, "green": 6, "blue": 6},
                "maximums": {"red": 1, "green": 3, "blue": 4},
            },
            12
        ],
        [
            {
                "number": 3,
                "rounds": [
                    [(8, "green"), (6, "blue"), (20, "red")],
                    [(5, "blue"), (4, "red"), (13, "green")],
                    [(5, "green"), (1, "red")],
                ],
                "totals": {"red": 25, "green": 26, "blue": 11},
                "maximums": {"red": 20, "green": 13, "blue": 6},
            },
            1560
        ],
        [
            {
                "number": 4,
                "rounds": [
                    [(1, "green"), (3, "red"), (6, "blue")],
                    [(3, "green"), (6, "red")],
                    [(3, "green"), (15, "blue"), (14, "red")],
                ],
                "totals": {"red": 23, "green": 7, "blue": 21},
                "maximums": {"red": 14, "green": 3, "blue": 15},
            },
            630
        ],
        [
            {
                "number": 5,
                "rounds": [
                    [(6, "red"), (1, "blue"), (3, "green")],
                    [(2, "blue"), (1, "red"), (2, "green")],
                ],
                "totals": {"red": 7, "green": 5, "blue": 3},
                "maximums": {"red": 6, "green": 3, "blue": 2},
            },
            36
        ]
])
def test_get_game_power(game, expected_power):
    assert get_game_power(game) == expected_power