"""Basic syntax of lists"""

my_numbers: list[float] = []

# add an item to the list
my_numbers.append(1.5)
my_numbers.append(2.3)
print(my_numbers)

# create an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# indexing
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# modifing list with index
game_points[1] = 72
print(game_points)


# finding te length of the lists
print(len(game_points))
print(game_points)

# removing an item
game_points.pop(2)
print(game_points)


def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


display(input=game_points)
