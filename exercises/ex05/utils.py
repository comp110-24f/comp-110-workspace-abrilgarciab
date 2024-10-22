"""Exercises using Unit tests!"""

__author__ = "730662458"


def only_evens(
    input_list: list[int],
) -> list[
    int
]:  # defines a function that will return a new list that has the even numbers from the input list
    new_list: list[int] = []  # used as an empty list that will have the even numbers
    for (
        elem
    ) in input_list:  # used a for loop to go through each number in the input list
        if elem % 2 == 0:  # used a remiander modulo to check is the number was even
            new_list.append(elem)  # the append will add the even nomber to the new list
    return new_list


def sub(
    input_list: list[int], start_idx: int, end_idx: int
) -> list[
    int
]:  # defines a function that will return a new list that is a subset of numbers between the start index and the end index
    new_list: list[int] = []  # empty list that will have the numbers in between
    len_of_list: int = len(
        input_list
    )  # used so that it gets the length of the input lis
    if start_idx < 0:  # used so that the start index is at least index 0
        start_idx = 0
    if (
        end_idx > len_of_list
    ):  # used so that the end index is maximum the length of the list
        end_idx = len_of_list
    if (
        len_of_list == 0 or start_idx >= len_of_list or end_idx <= 0
    ):  # used so that it returns an empty list if the start index is too big or if the end index is equal to the start index
        return new_list
    idx: int = start_idx
    while (
        idx < end_idx
    ):  # used so that the while loop will go through each index in the list starting from the start index and ending at the end index, adding all those values to the new list
        new_list.append(input_list[idx])
        idx += 1
    return new_list  # returns the new list


def add_at_index(
    input_list: list[int], elem_added: int, idx: int
) -> (
    None
):  # defines a function that will add an elemt at a index given in the input list
    if idx < 0 or idx > len(
        input_list
    ):  # used to check that the index is not less than 0 or greater than the length of the list
        raise IndexError(
            "Index is out of bounds for the input list"
        )  # if the bool comes out to True for either it will raise an index error
    input_list.append(
        0
    )  # used to add space at the end of the list if something has to get appended there
    index: int = len(input_list) - 1
    while (
        index > idx
    ):  # used to shift everything to the right of the index in order to make space for the element
        input_list[index] = input_list[index - 1]
        index = index - 1
    input_list[idx] = (
        elem_added  # needed so that the new element will go in the index given
    )
