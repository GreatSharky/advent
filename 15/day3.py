from dataclasses import dataclass
houses = {} # points, populate, calculate uniques
x = 0
y = 1

with open("input3.txt", "r") as file:
    point = "0,0"
    for char in file.readline().strip():
        if point in houses:
            houses[point] += 1
        else:
            houses[point] = 1
        if char == ">":
            cords = [int(x) for x in point.split(",")]
            point = f"{cords[x]+1},{cords[y]}"
        elif char == "<":
            cords = [int(x) for x in point.split(",")]
            point = f"{cords[x]-1},{cords[y]}"
        elif char == "^":
            cords = [int(x) for x in point.split(",")]
            point = f"{cords[x]},{cords[y]+1}"
        elif char == "v":
            cords = [int(x) for x in point.split(",")]
            point = f"{cords[x]},{cords[y]-1}"
    if point in houses:
        houses[point] += 1
    else:
        houses[point] = 1

print(len(houses))
