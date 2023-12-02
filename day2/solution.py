def split_line(line: str) -> dict:
    line_parts = line.split(":")
    game_rounds = line_parts[1].split(";")
    parsed_game = {
        "number": int(line_parts[0].strip().split(" ")[1]),
        "rounds": [],
        "totals": {"red": 0, "green": 0, "blue": 0},
        "maximums": {"red": 0, "green": 0, "blue": 0},
    }
    for round in game_rounds:
        round_blocks = round.split(",")
        parsed_round = []
        for block in round_blocks:
            count = int(block.strip().split(" ")[0])
            color = block.strip().split(" ")[1]
            parsed_round.append((count, color))
            if color == "red":
                parsed_game["totals"]["red"] += int(count)
                if int(count) > parsed_game["maximums"]["red"]:
                    parsed_game["maximums"]["red"] = int(count)
            elif color == "green":
                parsed_game["totals"]["green"] += int(count)
                if int(count) > parsed_game["maximums"]["green"]:
                    parsed_game["maximums"]["green"] = int(count)
            elif color == "blue":
                parsed_game["totals"]["blue"] += int(count)
                if int(count) > parsed_game["maximums"]["blue"]:
                    parsed_game["maximums"]["blue"] = int(count)
        parsed_game["rounds"].append(parsed_round)
    return parsed_game


def is_game_possible(game: dict, red_max: int, green_max: int, blue_max: int) -> bool:
    if game["maximums"]["red"] > red_max:
        return False
    if game["maximums"]["green"] > green_max:
        return False
    if game["maximums"]["blue"] > blue_max:
        return False
    return True


def get_game_power(game) -> int:
    return (
        game["maximums"]["red"] * game["maximums"]["green"] * game["maximums"]["blue"]
    )


if __name__ == "__main__":
    with open("day2/input") as f:
        lines = f.readlines()

    total_possible = 0
    total_power = 0
    for line in lines:
        game = split_line(line)
        if is_game_possible(game, 12, 13, 14):
            total_possible += game["number"]
        total_power += get_game_power(game)

    print(total_possible)
    print(total_power)
