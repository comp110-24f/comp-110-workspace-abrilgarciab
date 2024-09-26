def get_weather_report() -> str:
    """some stuff"""
    weather: str = input("What is the weather")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket")
    else:
        if weather == "hot":
            print("Keep cool out there!")
        else:
            print("I don't recognize this weather")
    return weather


def get_ticket_price() -> int:
    age: int = int(input("What is your age"))
    if age <= 12:
        price: int = 5
    else:
        price: int = 10
    return price
