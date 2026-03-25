"""A string with ( and ) is given as input. The output is a number"""

with open("input1.txt", "r") as file:
    guide = file.read()

floor = 0
cache = []
for direction in guide:
    if direction == '(':
        floor += 1
    elif direction == ')':
        floor -= 1
    cache.append(floor)
    
pos = cache.index(-1) + 1
print("Final floor", floor)
print("First pass", pos)
