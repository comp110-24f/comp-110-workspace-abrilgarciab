from CQs.cq07.find_max import find_and_remove_max

__author__ = "730662458"


def test_find_and_remove_max_val() -> None:
    b: list[int] = [10, 9, 8, 7, 10]
    assert find_and_remove_max(b) == 10


def test_find_and_remove_max_mutation() -> None:
    b: list[int] = [10, 9, 8, 7, 10]
    find_and_remove_max(b)
    assert (b) == [9, 8, 7]


def test_find_and_remove_max_emptylist() -> None:
    a: list[int] = []
    assert find_and_remove_max(a) == -1
    assert a == []
