from dataclasses import dataclass
x = 0
y = 1

with open("input3.txt", "r") as file:
    point = "0,0"
    santa = [point]
    robo_santa = [point]
    for i, char in enumerate(file.readline().strip()):
        houses = santa if i % 2 == 0 else robo_santa
        point = houses[-1]
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
        houses.append(point)

santa.extend(robo_santa)
print(len(set(santa)))
