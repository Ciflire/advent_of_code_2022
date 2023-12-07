import sys

def day2_1(input):
    file = open(input, mode='r')
    all_of_it = file.read()
    list_of_actions = all_of_it.split("\n")
    score = 0
    points_issue = [0, 3, 6]
    points_shape = {"X": 1, "Y": 2, "Z": 3}
    for elt in list_of_actions:
        score += points_issue[match(elt)] + points_shape[elt[2]]
        print(score)
    return score

def match(elt):
    map = {
        "A X": 1,
        "A Y": 2,
        "A Z": 0,
        "B X": 0,
        "B Y": 1,
        "B Z": 2,
        "C X": 2,
        "C Y": 0,
        "C Z": 1
    }
    return map[elt]



print(day2_1("/home/ciflire/Documents/adventofcode/advent_of_code_2022/day2/input.txt"))
