import numpy as np

def task1():
    def off(grid: np.ndarray, points: list[list[int,int],list[int,int]]):
        grid[points[0][0]:points[1][0], points[0][1]:points[1][1]] = 0
        return grid

    def on(grid: np.ndarray, points: list[list[int,int],list[int,int]]):
        grid[points[0][0]:points[1][0], points[0][1]:points[1][1]] = 1
        return grid

    def toggle(grid: np.ndarray, points: list[list[int,int],list[int,int]]):
        grid[points[0][0]:points[1][0], points[0][1]:points[1][1]] ^=1
        return grid

    def points(start, end):
        start = [int(c) for c in start.split(',')]
        end = [int(c)+1 for c in end.split(',')]
        return [start, end]

    with open("inputs/input6.txt", "r") as file:
        instructions = file.readlines()

    grid = np.zeros((1000,1000),int)

    for instruction in instructions:
        instruction = instruction.rstrip()
        if instruction.startswith("toggle"):
            data = instruction.split(" ")
            start = data[1]
            end = data[3]
            grid = toggle(grid, points(start,end))
        elif instruction.startswith("turn on"):
            data = instruction.split(' ')
            start = data[2]
            end = data[-1]
            grid = on(grid, points(start,end))
        elif instruction.startswith("turn off"):
            data = instruction.split(' ')
            start = data[2]
            end = data[-1]
            grid = off(grid, points(start,end))
        debugsum = grid.sum()

    return grid.sum()

def task2():
    def off(grid: np.ndarray, points: list[list[int,int],list[int,int]]):
        subgrid = grid[points[0][0]:points[1][0], points[0][1]:points[1][1]]
        subgrid[:] = np.clip(subgrid - 1, 0, None)
        return grid

    def on(grid: np.ndarray, points: list[list[int,int],list[int,int]]):
        grid[points[0][0]:points[1][0], points[0][1]:points[1][1]] += 1
        return grid

    def toggle(grid: np.ndarray, points: list[list[int,int],list[int,int]]):
        grid[points[0][0]:points[1][0], points[0][1]:points[1][1]] += 2
        return grid

    def points(start, end):
        start = [int(c) for c in start.split(',')]
        end = [int(c)+1 for c in end.split(',')]
        return [start, end]

    with open("inputs/input6.txt", "r") as file:
        instructions = file.readlines()

    grid = np.zeros((1000,1000),np.int64)

    for instruction in instructions:
        instruction = instruction.rstrip()
        if instruction.startswith("toggle"):
            data = instruction.split(" ")
            start = data[1]
            end = data[3]
            grid = toggle(grid, points(start,end))
        elif instruction.startswith("turn on"):
            data = instruction.split(' ')
            start = data[2]
            end = data[-1]
            grid = on(grid, points(start,end))
        elif instruction.startswith("turn off"):
            data = instruction.split(' ')
            start = data[2]
            end = data[-1]
            grid = off(grid, points(start,end))

    return grid.sum()


print(task1())
print(task2())
