from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""Exercises using Unit tests!"""

__author__ = "730662458"


# tests if the only_evens function works at returning the even numbers in the list
def test_only_evens_works() -> None:
    input_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(input_list) == [2, 4, 6]


# tests if the only_even function will return an empty list when only odd numbers are given in the input list
def test_only_evens_odd_num_only() -> None:
    input_list: list[int] = [
        1,
        3,
        5,
    ]
    assert only_evens(input_list) == []


#  tests if only_evens returns an empty list when the input list is empty
def test_only_evens_empty() -> None:
    assert only_evens([]) == []


# tests if the sub function will return the list starting from the beginning of the list even if the start index is a negative number
def test_sub_neg_index() -> None:
    input_list: list[int] = [10, 20, 30, 40]
    assert sub(input_list, -1, 4) == [10, 20, 30, 40]


# tests if sub will return the correct list even if the end index is a number greater than the length of the list
def test_sub_greater_len_of_list() -> None:
    input_list: list[int] = [10, 20, 30, 40]
    assert sub(input_list, 0, 6) == [10, 20, 30, 40]


# test if sub will return an empty list when the input list is empty
def test_sub_empty() -> None:
    assert sub([], 0, 3) == []


# tests if add_at_index will work correctly in adding the element in the index given
def test_add_at_index_works() -> None:
    input_list: list[int] = [1, 2, 3, 5]
    add_at_index(input_list, 4, 3)
    assert input_list == [1, 2, 3, 4, 5]


# test if add_at_index will return a list with the element when the input list is empty at index 0
def test_add_at_index_empty() -> None:
    input_list: list[int] = []
    add_at_index(input_list, 1, 0)
    assert input_list == [1]


# tests if add_at_index raises the Index Error when the index given is invalid/out of range
def test_add_at_index_raises_indexerror():
    input_list: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(input_list, 1, 1)
