"""Exercise with list unitls"""

__author__ = "730662458"


def all(
    list_int: list[int], given_int: int
) -> bool:  # Uses a bool to return true if all the
    # intergers in the list match the given_int
    index: int = 0
    if len(list_int) == 0:  # used to check if the list is empty
        return False
    while index < len(
        list_int
    ):  # a condition that is used to loop through the statements
        if (
            list_int[index] == given_int
        ):  # used to check if the current index is equal to the given int
            index += 1
        else:
            return False  # returns false if the index and given_int does not match
    return True  # returns true is all the indexes in the list match the given_int


def max(
    list_int: list[int],
) -> int:  # a function that will return the largest int in the list
    if len(list_int) == 0:
        raise ValueError("max() arg is an empty List")  # used to say the list is empty
    index: int = (
        1  # used to start from the first index bc it will be compared to the first element
    )
    largest_int: int = list_int[0]  # assumes the first int is the largest
    while index < len(list_int):
        if (
            list_int[index] > largest_int
        ):  # used to compare the first int in the list to the current largest_int
            largest_int = list_int[
                index
            ]  # used to update the current largest_int of one is found
        index += 1
    return largest_int  # returns the largest int in the list


def is_equal(
    list1: list[int], list2: list[int]
) -> bool:  # used to return a bool of True
    # if every element at every index is equal in both list
    if not (
        len(list1) == len(list2)
    ):  # needed to check if both list are of equal length first
        # before it compares the elements at each index
        return False
    index: int = 0  # used to be able to compare the indexes
    while index < len(list1):  # used to loop through all the elements in each list
        if not (
            list1[index] == list2[index]
        ):  # if the elements at each index are not equal it will return false
            return False
        index += 1
    return True  # if does not return then instead true


def extend(
    list1: list[int], list2: list[int]
) -> None:  # uses the extend function to mutate list1 by appending values of list2
    # to the end of list1.
    index: int = 0
    while index < len(list2):  # used to go through all the elements in list 2
        list1.append(list2[index])  # now to append all those elements into list 1
        index += 1
