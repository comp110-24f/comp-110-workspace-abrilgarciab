"""Exercise 01: Planning a tea party """

__author__: str = "730662458"


def main_planner(guest: int) -> None:
    """Defines the 'main_planner' function and will print the outputs."""
    print("A cozy Tea Party for " + str(guest) + " People")
    print("Tea Bags: " + str(tea_bags(people=guest)))
    print("Treats: " + str(treats(people=guest)))
    print(
        "Cost: $"
        + str(cost(tea_count=tea_bags(people=guest), treat_count=treats(people=guest)))
    )


def tea_bags(people: int) -> int:
    """Defines the function 'tea_bags' and calculates the number of tea bags needed based on the # of people"""
    return (
        people * 2
    )  # Once a value for 'people" is recieved it returns a value for the number of tea_bags by doing 'people * 2'


def treats(people: int) -> int:
    """Defines the function 'treats' and calculates the number of treats based off the # of people.
    Assumes each person will eat 1.5 treats with their tea"""
    return int(
        tea_bags(people=people) * 1.5
    )  # calls 'tea_bags', once a return value is recieved it is then multiplied by 1.5


def cost(tea_count: int, treat_count: int) -> float:
    """Defines the function 'cost' and calculates the totals cost of tea_count and treat_count and returns a float"""
    return (
        tea_count * 0.50 + treat_count * 0.75
    )  # uses the parameter 'tea_count' and 'treat_count' to multiply them by their price and get added to get a return value of the cost


if __name__ == "__main__":
    main_planner(guest=int(input("How many guest are attending your tea party? ")))
