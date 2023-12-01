import re

# Load file
with open('day1/input', 'r') as f:
    data = f.readlines()

part1_calibrations = []

for line in data:
    calibration = ""
    # Find first digit in string
    for character in line:
        if character.isdigit():
            calibration += character
            break
    
    # Find last digit in string
    for character in reversed(line):
        if character.isdigit():
            calibration += character
            break
    part1_calibrations.append(int(calibration))

print(sum(part1_calibrations))

part2_calibrations = []

digit_finder = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|zero|\d))')

def convert_to_digit(value: str) -> str:
    match value:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case _:
            return value

# Part 2
for line in data:
    calibration = ""
    matches = digit_finder.findall(line)
    # Find first digit in string
    calibration += convert_to_digit(matches[0])
    # Find last digit in string
    calibration += convert_to_digit(matches[-1])
    part2_calibrations.append(int(calibration))

print(sum(part2_calibrations))