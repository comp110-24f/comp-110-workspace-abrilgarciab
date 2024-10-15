"""Summing the elements of a list using different loops"""

__author__ = "730662458"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum = sum + vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for elem in vals:
        sum = sum + elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for elem in range(0, len(vals)):
        sum = sum + elem
    return sum
