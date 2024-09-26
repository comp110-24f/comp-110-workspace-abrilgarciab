"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730662458"


def input_word() -> str:  # defines the function input_word that
    # gathers input from a the user
    word: str = input("Enter a 5-character word: ")  # the variable
    # used for a 5 character word input from user
    if not len(word) == 5:
        print("Error: Word must contain 5 characters.")  # lets the user
        # know that their input does not match the 5 character requirment
        exit()
    return word


def input_letter() -> str:  # defines the function input_letter that
    # gathers a single character input from the user
    letter: str = input("Enter a single character: ")  # the variable
    # used for a single character input from user
    if not len(letter) == 1:
        print("Error: Character must be a single character.")  # lets the user
        # know that their inout does not match the single character requirement
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:  # defines the function contains_char
    # that checks if the input_letter matches any of the indices in the input_word
    count: int = 0  # a local variable used to count the number of instances the letter
    # appears in the word
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:  # in lines 33-47 are checking each of the 5 indices of the
        # word str to see if it is the same as the character str
        print(letter + " found at index " + str(0))
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index " + str(1))
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index " + str(2))
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index " + str(3))
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index " + str(4))
        count = count + 1

    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instances of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


# counting the number of matching instances line 50-55


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
