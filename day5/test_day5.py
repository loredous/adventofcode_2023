from pytest import mark
from day5.solution import generate_map_part, input_to_maps, generate_map_sections

example_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def test_input_to_maps():
    result = input_to_maps(example_input)
    assert result['seeds'] == [79, 14, 55, 13]
    

@mark.parametrize("input, expected", [
    ["50 98 2", {"start":98, "end":99, "transform":-48}],
    ["52 50 48", {"start":50, "end":97, "transform":2}],
    ["0 15 37", {"start":15, "end":51, "transform":-15}],
    ["37 52 2", {"start":52, "end":53, "transform":-15}],
])
def test_generate_map_part(input, expected):
    result = generate_map_part(input)
    assert result == expected

def test_generate_map_sections():
    expected_sections = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
    
    result = generate_map_sections(example_input.split("\n\n")[1:])
    
    assert all([section in result.keys() for section in expected_sections])