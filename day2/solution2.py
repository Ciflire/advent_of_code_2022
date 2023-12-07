import sys

def day2_1(input):
    file = open(input, mode='r')
    all_of_it = file.read()
    list_of_actions = all_of_it.split("\n")[0:-1]
    score = 0
    points_match = {"X": 0, "Y": 3, "Z": 6}
    points_shape = {
        "A X": 3,
        "A Y": 1,
        "A Z": 2,
        "B X": 1,
        "B Y": 2,
        "B Z": 3,
        "C X": 2,
        "C Y": 3,
        "C Z": 1
    }
    for elt in list_of_actions:
        score += points_shape[elt] + points_match[elt[2]]
        print(score)
    return score

print(day2_1("/home/ciflire/Documents/adventofcode/advent_of_code_2022/day2/input.txt"))
