
from typing import List, Dict, Tuple
import multiprocessing


def input_to_maps(input) -> Dict:
    result = {}
    sections = input.split("\n\n")
    # Seed list
    seeds = sections[0].split(" ")[1:]
    result['seeds'] = [int(seed) for seed in seeds]
    # Map sections
    result.update(generate_map_sections(sections[1:]))
    return result

def generate_map_sections(inputs: list) -> Dict:
    result = {}
    for input in inputs:
        lines = input.split("\n")
        section_name = lines[0].split(" ")[0]
        section_data = []
        for line in lines[1:]:
            if line == "":
                continue
            section_data.append(generate_map_part(line))
        result[section_name] = section_data
    return result

def generate_map_part(input: str) -> Dict:
    dest_start, src_start, len = input.split(" ")
    result = {"start":int(src_start), "end":int(src_start)+int(len)-1, "transform": int(dest_start)-int(src_start)}
    return result

def do_mapping(input, map: List) -> int:
    for map_part in map:
        if map_part['start'] <= input <= map_part['end']:
            return input + map_part['transform']
    return input

def do_reverse_mapping(input, map: List) -> int:
    for map_part in map:
        if map_part['start'] <= input - map_part['transform'] <= map_part['end']:
            return input - map_part['transform']
    return input

def maps_to_chains(maps: Dict) -> Dict:
    result = {}
    for seed in maps['seeds']:
        chain = {}
        chain['soil'] = do_mapping(seed, maps['seed-to-soil'])
        chain['fertilizer'] = do_mapping(chain['soil'], maps['soil-to-fertilizer'])
        chain['water'] = do_mapping(chain['fertilizer'], maps['fertilizer-to-water'])
        chain['light'] = do_mapping(chain['water'], maps['water-to-light'])
        chain['temperature'] = do_mapping(chain['light'], maps['light-to-temperature'])
        chain['humidity'] = do_mapping(chain['temperature'], maps['temperature-to-humidity'])
        chain['location'] = do_mapping(chain['humidity'], maps['humidity-to-location'])
        result[seed] = chain
    return result

def get_seed_from_location(location, maps: Dict) -> int:
    humidity = do_reverse_mapping(location, maps['humidity-to-location'])
    temperature = do_reverse_mapping(humidity, maps['temperature-to-humidity'])
    light = do_reverse_mapping(temperature, maps['light-to-temperature'])
    water = do_reverse_mapping(light, maps['water-to-light'])
    fertilizer = do_reverse_mapping(water, maps['fertilizer-to-water'])
    soil = do_reverse_mapping(fertilizer, maps['soil-to-fertilizer'])
    seed = do_reverse_mapping(soil, maps['seed-to-soil'])
    return seed
        
def bf_test_range(min, max, maps, seed_ranges) -> int:
    for loc in range(min,max):
        seed = get_seed_from_location(loc, maps)
        if seed < 0:
            continue
        if any([seed_range[0] <= seed <= seed_range[1] for seed_range in seed_ranges]):
            print(loc)
            return loc
    return None

if __name__ == "__main__":
    with open("day5/input") as f:
        data = f.read()

    maps = input_to_maps(data)
    chains = maps_to_chains(maps)
    locations = [chain['location'] for chain in chains.values()]
    print(min(locations))

    seed_ranges = []
    for i in range(0, len(maps['seeds']),2):
        seed_ranges.append((maps['seeds'][i], maps['seeds'][i]+maps['seeds'][i+1]))
    

    #gross brute force solution
    max_processes = multiprocessing.cpu_count() - 5
    with multiprocessing.Pool(max_processes) as pool:
        location = 102000000
        current_processes = []
        while True:
            if len(current_processes) < max_processes:
                current_processes.append(pool.apply_async(bf_test_range, (location, location+100000, maps, seed_ranges)))
                location += 100000
            else:
                for process in current_processes:
                    if process.ready():
                        result = process.get()
                        if result:
                            print(result)
                            exit(0)
                        current_processes.remove(process)
        
        
