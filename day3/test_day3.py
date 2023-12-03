from pytest import mark, fixture
from day3.solution import EngineSchematic

@fixture
def test_engine_schematic():
    schematic_data = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    return EngineSchematic(schematic_data)

@mark.parametrize(
    "x, y, expected",
    [
        [0, 2, True],
        [0, 5, False],
        [2, 2, True],
        [2, 3, True],
        [2, 6, True],
        [2, 8, False],
        [4, 2, True],
        [5, 7, False],
        [5, 8, False],
        [6, 4, True],
    ]
)
def test_is_touching_symbol(test_engine_schematic, x, y, expected):
    assert test_engine_schematic.is_touching_symbol(x, y) == expected

def test_get_sum(test_engine_schematic):
    assert test_engine_schematic.get_part_number_sum() == 4361

@mark.parametrize(
    "x, y, expected",
    [
        [0, 2, [('*', 1, 3)]],
        [2, 2, [('*', 1, 3)]],
        [2, 3, [('*', 1, 3)]],
        [2, 6, [('#', 3, 6)]],
        [4, 2, [('*', 4, 3)]],
        [6, 4, [('+', 5, 5)]],
    ]
)
def test_get_touching_symbols(test_engine_schematic, x, y, expected):
    assert test_engine_schematic.get_touching_symbols(x, y) == expected

def test_get_gear_ratio_sum(test_engine_schematic):
    assert test_engine_schematic.get_gear_ratio_sum() == 467835