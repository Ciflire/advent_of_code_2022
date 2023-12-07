import sys

def day1_1(input):
    file = open(input, mode='r')
    all_of_it = file.read()
    list_of_elves = all_of_it.split("\n\n")
    max = 0
    for elt in list_of_elves:
        listToSum = [int(i) for i in elt.split("\n") if i.isdigit()]
        sumList = 0
        sumList = sum(listToSum)
        if sumList >= max:
            max = sumList
    # n = all_of_it.count("\n\n")
    return max

def day1_2(input):
    file = open(input, mode='r')
    all_of_it = file.read()
    list_of_elves = all_of_it.split("\n\n")
    treeBest = [0] * 3

def day1_2(input):
    file = open(input, mode='r')
    all_of_it = file.read()
    list_of_elves = all_of_it.split("\n\n")
    treeBest = [0] * 3
    for elt in list_of_elves:
        listToSum = [int(i) for i in elt.split("\n") if i.isdigit()]
        sumList = 0
        sumList = sum(listToSum)
        if sumList >= treeBest[0]:
            treeBest[2] = treeBest[1]
            treeBest[1] = treeBest[0]
            treeBest[0] = sumList
        elif sumList >= treeBest[1]:
            treeBest[2] = treeBest[1]
            treeBest[1] = sumList
        elif sumList >= treeBest[2]:
            treeBest[2] = sumList
    return treeBest[0] + treeBest[1] + treeBest[2]


print(day1_2("/home/ciflire/Documents/adventofcode/advent_of_code_2022/day1/input.txt"))


