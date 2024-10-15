"""Practicing for loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]
for elem in pets:
    print(f"Good boy, {elem}!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for index in range(0, len(names)):
    print(f"{index}: {names[index]}")


for x in [1, 2, 3]:
    print(x)
