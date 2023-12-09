from typing import List


def generate_difference_list(numbers):
    difference_list = []
    for i in range(len(numbers) - 1):
        difference_list.append(numbers[i+1] - numbers[i])
    return difference_list

def generate_prediction_pyramid(values) -> List[List[int]]:
    pyramid = []
    pyramid.append(values)
    while True:
        pyramid.append(generate_difference_list(pyramid[-1]))
        if not any(pyramid[-1]):
            return pyramid
    
def generate_prediction(pyramid: List[List[int]]) -> int:
    for i in range(len(pyramid) - 1, 0, -1):
        pyramid[i - 1].append(pyramid[i][-1] + pyramid[i - 1][-1])
    return pyramid[0][-1]

def generate_backward_prediction(pyramid: List[List[int]]) -> int:
    for i in range(len(pyramid) - 1, 0, -1):
        pyramid[i - 1].insert(0, pyramid[i - 1][0] - pyramid[i][0])
    return pyramid[0][0]

if __name__ == "__main__":
    with open("day9/input") as f:
        readings = f.readlines()
    total = 0
    for reading in readings:
        numbers = [int(number) for number in reading.split()]
        pyramid = generate_prediction_pyramid(numbers)
        total += generate_prediction(pyramid)
    print(total)

    total2 = 0
    for reading in readings:
        numbers = [int(number) for number in reading.split()]
        pyramid = generate_prediction_pyramid(numbers)
        total2 += generate_backward_prediction(pyramid)
    print(total2)