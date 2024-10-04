"""Creation of my own wordle game"""

__author__ = "730662458"


def input_guess(secret_word_len: int) -> str:  # defines the function input_guess
    # that prompts a user for a guess as input
    guess: str = input(f"Enter a {secret_word_len} character word: ")  # the variable
    # is used as a way to take the guess inputed and return it if its the length needed
    while not len(guess) == secret_word_len:
        guess = input(
            f"That wasn't {secret_word_len} chars! Try again: "
        )  # used if the
        # guess inputed is not the length needed
    return guess


def contains_char(sec_word: str, char: str) -> bool:
    """The function defined will look through each index to search
    for the character in the word and returns True if found and False if not"""
    assert len(char) == 1
    index: int = 0  # is a variable that helps store the index needed
    while index < len(sec_word):  # the while loop helps check each index of the secret
        # word to see if it is less than the index
        if sec_word[index] == char:
            return True  # if the bool statment comes out to be true that means that the
        # the character was found in the secret word
        index = index + 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """The function defined will compare the guess with the secret and
    will return a str of emojis whether the guess was correct"""
    assert len(user_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    index: int = 0
    wordle: str = ""  # a local variable that is used as an empty string to
    # store the emojis
    while index < len(
        user_guess
    ):  # while loop used to go through each chracter in the user_guess
        if (
            user_guess[index] == secret_word[index]
        ):  # a conditional that makes sure the letter
            # at that index matches the one in the secret word and returns true it will print the green box emoji
            wordle = wordle + GREEN_BOX
        elif contains_char(
            secret_word, user_guess[index]
        ):  # else if it does not match at that
            # specifc index but is in another index it prints the yello box emoji
            wordle = wordle + YELLOW_BOX
        else:
            wordle = wordle + WHITE_BOX  # if niether it returns the white box emoji
        index = index + 1
    return wordle  # returns all the white,yellow, and green boxes that aligned with the user_guess and secret_word as a string


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    num_of_turns: int = 1  # local variable that tracks the number of turns
    max_turns: int = 6  # local variable used to allow a maximum number of turn
    won_game: bool = False  # local variable used to track if the game was won
    while (
        num_of_turns <= max_turns and not won_game
    ):  # while loop needed to run the game until the turns run out or secret word
        # is guessed correctly
        print(f"=== Turn {num_of_turns}/{max_turns} ===")
        user_guess: str = input_guess(
            len(secret_word)
        )  # prompts the user for an input of a word of the correct length
        print(
            emojified(user_guess, secret_word)
        )  # calls the emojified function to print the emoji box color to the letter in the
        # secret word and the guess
        if user_guess == secret_word:
            won_game = (
                True  # needed to check if the used guessed the secret_word correctly
            )
        else:
            num_of_turns = num_of_turns + 1
    if won_game:
        print(
            f"You won in {num_of_turns}/{max_turns} turns!"
        )  # prints the num of turn it took to win
    else:
        print(
            f"X/{max_turns} - Sorry, try again tomorrow!"
        )  # prints of you ran out of turns by not guessing correctly


if __name__ == "__main__":
    main(secret_word="codes")
