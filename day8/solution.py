from dataclasses import dataclass
import math


def build_map(data) -> dict:
    map = {}
    for line in data:
        if line == "": continue
        node = line[0:3]
        left = line[7:10]
        right = line[12:15]
        map[node] = {"left": left, "right": right}
    return map

def walk_map(map: dict, pattern: str, starting_node: str = "AAA", final_node: str = "ZZZ") -> int:
    current_node = starting_node
    step_count = 0
    while current_node != final_node:
        if pattern[step_count%len(pattern)] == "L":
            current_node = map[current_node]["left"]
        else:
            current_node = map[current_node]["right"]
        step_count += 1
    return step_count

def part2_walker(map: dict, pattern: str, starting_suffix: str = "A", final_suffix: str = "Z") -> int:
    starting_nodes = []
    for node in map:
        if node.endswith(starting_suffix):
            starting_nodes.append(node)
    step_counts = []
    for start in starting_nodes:
        current_node = start
        step_count = 0
        while not current_node.endswith(final_suffix):
            if pattern[step_count%len(pattern)] == "L":
                current_node = map[current_node]["left"]
            else:
                current_node = map[current_node]["right"]
            step_count += 1
        step_counts.append(step_count)
    return math.lcm(*step_counts)

if __name__ == "__main__":
    with open("day8/input") as f:
        data = f.readlines()
    map = build_map(data[2:])
    pattern = data[0].strip()
    print(walk_map(map, pattern))
    print(part2_walker(map, pattern))