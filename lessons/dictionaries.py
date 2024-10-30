"""Examples of dicitonary syntax with Ice Cream Shop order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawbery": 5,
}
print(f"{len(ice_cream)} flavors")

ice_cream["mint"] = 3

print(ice_cream["chocolate"])

ice_cream["vanilla"] = 10

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no order of mint")

ice_cream.pop("strawberry")

for flavor in ice_cream:
    print(f"{flavor}: {ice_cream[flavor]}")
    total_orders += ice_cream[flavor]
print(f"Total_orders: {total_orders}")
