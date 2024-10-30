"""Exercise 06 using dictionaries"""

__author__ = "730662458"


def invert(
    input_dict: dict[str, str]
) -> dict[
    str, str
]:  # a function that will invert the keys & values from an input dictionary and put them in a new list
    inverted_dict: dict[str, str] = (
        {}
    )  # an empty dicitonary that will have the keys and values that were inverted
    for key in input_dict:  # a for loop to go through each key in input_dict
        value = input_dict[key]  # used so that the value is now what they key was
        if (
            value in inverted_dict
        ):  # used to check if the value already exist as a key and if it does then it will raise a KeyError
            raise KeyError(f"Duplicate key found when inverting: '{value}' ")
        inverted_dict[value] = (
            key  # will add the new inverted keys and values to the inverted_dict
        )
    return inverted_dict


def favorite_color(
    color_dict: dict[str, str]
) -> str:  # a function that will return a str of what color is the most popular
    count: dict[str, int] = (
        {}
    )  # used as a dictionary that will the number of times each color is in the dict
    most_pop: str = ""  # a variable to store the most popular color as an empty
    max_count: int = (
        0  # a varibale that will store the amount of times just the most popular color is in the dict
    )
    for name in color_dict:
        color_name = color_dict[
            name
        ]  # used to get the very first key which is name and its value which is color
        if (
            color_name in count
        ):  # used to increase or keep the amount of times the color is mentioned the same in the dict
            count[color_name] += 1
        else:
            count[color_name] = 1
        if (
            count[color_name] > max_count
        ):  # used to chnage the most poopular color if the count of that color is greater than max_count
            most_pop = color_name
            max_count = count[
                color_name
            ]  # also used so that if there is a ties whichever color came first is the most_pop
    return most_pop


def count(
    input_list: list[str],
) -> dict[
    str, int
]:  # a function that returns a dict that will have the values of the list as keys in the dict and the values in the dict will be the count of times they appear
    empty_dict: dict[str, int] = (
        {}
    )  # an empty dict that will store the count of the times the value appears in the list
    for (
        value
    ) in input_list:  # uses a for loop to go through each value in the input list
        if (
            value in empty_dict
        ):  # used to check if the value is already a key in the empty_dict
            empty_dict[value] += 1  # increases if the value appeares more than once
        else:
            empty_dict[value] = 1  # count stays at one if it only appears once
    return empty_dict


def alphabetizer(
    input_list: list[str],
) -> dict[
    str, list[str]
]:  # a function that return a dict that will have letters as keys and have its values be lists of words that begin with that letter
    empty_dict: dict[str, list[str]] = (
        {}
    )  # creates an empty dict that will be stored letters as keys and list of words as values
    for word in input_list:  # uses a for loop to go through each word in the list
        first_letter = word[
            0
        ].lower()  # used to get the first letter of every word by using the first index
        if (
            first_letter in empty_dict
        ):  # used to check if the letter is not already a key in the empty_dict
            empty_dict[first_letter].append(
                word
            )  # if the firsy letter of the word is already in the empty_dict it will add the word to the list
        else:
            empty_dict[first_letter] = [
                word
            ]  # if the letter is not already in the empty_dict it will add it as a key and start the list with the word
    return empty_dict


def update_attendance(
    attendance: dict[str, list[str]], day_of_week: str, student_name: str
) -> None:
    # a function that will allow for an input dictionary that containes the days of the week and a list of students present that day to be updated by mutating the dict
    if (day_of_week) in (
        attendance
    ):  # used to check a key corresponding to the day of the week exists in the dictionary
        attendance[day_of_week].append(
            student_name
        )  # if the key already exist it will all the student's name to the existing list
    else:
        # if the day of the week is not already a key it will add it to the dictionary and create the list with the student's name
        attendance[day_of_week] = [student_name]
