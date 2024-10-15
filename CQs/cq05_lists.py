"""Mutating functions."""

__author__ = "730662458"


def manual_append(list1: list[int], index_value: int) -> None:
    list1.append(index_value)


def double(list1: list[int]) -> None:
    index: int = 0
    while index < len(list1):
        list1[index] = list1[index] * 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
