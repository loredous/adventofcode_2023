from math import ceil


def calculate_distance(hold_time, total_time):
    return hold_time * (total_time-hold_time)

def find_minmax_winner(total_time, winning_distance, minimum=True):
    test_value = 1 if minimum else total_time-1
    adjust = int(total_time/2)
    while adjust > 0:
        adjust = round(adjust/2)
        winner = calculate_distance(test_value, total_time) > winning_distance
        if winner:
            test_value = test_value-adjust if minimum else test_value+adjust
        else:
            test_value = test_value+(adjust or 1) if minimum else test_value-(adjust or 1)
    return test_value
            

if __name__ == "__main__":
    with open("day6/input") as f:
        lines = f.readlines()

    # Part 1
    times = [int(time) for time in lines[0].split(" ")[1:] if time != ""]
    distances = [int(distance) for distance in lines[1].split(" ")[1:] if distance != ""]
    total = 1
    for time,distance in zip(times,distances):
        minimum = find_minmax_winner(time, distance, True)
        maximum = find_minmax_winner(time, distance, False)
        count = maximum-minimum + 1
        print(f'min:{minimum} max:{maximum} count:{count}')
        total *= count
    print(total)

    # Part 2
    time = int("".join([time for time in lines[0].split(" ")[1:] if time != ""]))
    distance = int("".join([distance for distance in lines[1].split(" ")[1:] if distance != ""]))
    minimum = find_minmax_winner(time, distance, True)
    maximum = find_minmax_winner(time, distance, False)
    count = maximum-minimum + 1
    print(count)
