import sys

def day3_1(input):
    file = open(input, mode='r')
    all_of_it = file.read()
    list_of_rucks = all_of_it.split("\n")


def points(c:chr)->int:
    # construct a map of letters to numbers a = 1 to Z = 52
    map_points = {chr(i):i-96 for i in range(97,123), chr(i):i-38 for i in range(65,91)}
    return map_points

print(points('a'))

