from day8.solution import build_map, part2_walker, walk_map
from pytest import mark

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)


@mark.parametrize("input, expected", [
    [["AAA = (BBB, CCC)"], {"AAA": {"left": "BBB", "right": "CCC"}}],
    [["AAA = (BBB, CCC)", "BBB = (DDD, EEE)"], {"AAA": {"left": "BBB", "right": "CCC"}, "BBB": {"left": "DDD", "right": "EEE"}}],
    [["AAA = (BBB, CCC)", "BBB = (DDD, EEE)", "CCC = (ZZZ, GGG)"], {"AAA": {"left": "BBB", "right": "CCC"}, "BBB": {"left": "DDD", "right": "EEE"}, "CCC": {"left": "ZZZ", "right": "GGG"}}],
])
def test_build_map(input, expected):
    assert build_map(input) == expected

@mark.parametrize("input, pattern, expected", [
    [["AAA = (BBB, CCC)", "BBB = (DDD, EEE)", "CCC = (ZZZ, GGG)", "DDD = (DDD, DDD)", "EEE = (EEE, EEE)", "GGG = (GGG, GGG)", "ZZZ = (ZZZ, ZZZ)"], "RL", 2],
    [["AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"], "LLR", 6],
])
def test_walk_map(input, pattern, expected):
    map = build_map(input)
    assert walk_map(map, pattern) == expected

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)

@mark.parametrize("input, pattern, expected", [
    [["11A = (11B, XXX)", "11B = (XXX, 11Z)", "11Z = (11B, XXX)", "22A = (22B, XXX)", "22B = (22C, 22C)", "22C = (22Z, 22Z)", "22Z = (22B, 22B)", "XXX = (XXX, XXX)"], "LR", 6],
])
def test_walk_map_part2(input, pattern, expected):
    map = build_map(input)
    assert part2_walker(map, pattern, "A", "Z") == expected