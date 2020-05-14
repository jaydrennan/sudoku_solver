import print_format
import copy

original = [
    [4, 6, 9, 7, 5, 0, 3, 0, 0],
    [0, 0, 0, 2, 3, 0, 0, 9, 5],
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 8, 0, 9, 3, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 1, 7, 0, 8, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [9, 7, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 1, 0, 4, 6, 9, 7, 3],
]

wip = copy.deepcopy(original)

print("Starting Array:")

print_format.print_nice(original)

