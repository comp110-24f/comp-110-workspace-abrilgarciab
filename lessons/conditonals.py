"""Practicing condionals"""


def less_than_10(num: int) -> bool:
    """tell us if num < 10."""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("small number")
    else:
        print("Big number")
    print("Have a nice day")


less_than_10(num=7)

print(less_than_10(num=2))


def wake_up(alarm: bool) -> str:
    """return a message based on if alarm is going off"""

    if alarm is True:
        return "Wake up! Go to Comp 110"
    else:
        return "Keep sleeping. You deserve it. :)"


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter is first character of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
