""""Challenge question 7 unit tests"""

__author__ = "730662458"


def find_and_remove_max(input: list[int]) -> int:
    if len(input) == 0:
        return -1
    max_val: int = input[0]
    index: int = 1
    while index < len(input):
        if input[index] > max_val:
            max_val = input[index]
        index = index + 1
    idx: int = 0
    while idx < len(input):
        if input[idx] == max_val:
            input.pop(idx)
        else:
            idx = idx + 1
    return max_val
