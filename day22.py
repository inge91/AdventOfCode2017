from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

def load_grid(f):
    grid = []
    lines = open(f)
    for line in lines:
        grid.append(list(line[:-1]))
    return grid

def print_grid(grid, x, y):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if i == y and j == x:
                print("[", end='')
            else:
                print(" ", end='')
            print(grid[i][j], end ='')
            if i == y and j == x:
                print("]", end='')
            else:
                print(" ", end='')

        print("")
    print("")
    
def turn(currentDirection, turn_direction):
    if currentDirection == Direction.UP:
        if turn_direction == Direction.LEFT:
            return Direction.LEFT
        if turn_direction == Direction.RIGHT:
            return Direction.RIGHT
    if currentDirection == Direction.DOWN:
        if turn_direction == Direction.RIGHT:
            return Direction.LEFT
        if turn_direction == Direction.LEFT:
            return Direction.RIGHT
    if currentDirection == Direction.LEFT:
        if turn_direction == Direction.RIGHT:
            return Direction.UP
        if turn_direction == Direction.LEFT:
            return Direction.DOWN
    if currentDirection == Direction.RIGHT:
        if turn_direction == Direction.RIGHT:
            return Direction.DOWN
        if turn_direction == Direction.LEFT:
            return Direction.UP

def move(currentDirection, x,y, grid):
    if currentDirection == Direction.DOWN:
        if y == len(grid)-1:
            grid += [list('.' * len(grid[0]))]
        y+=1
    if currentDirection == Direction.LEFT:
        if x == 0:
            for i in range(0, len(grid)):
                grid[i] = ['.'] + grid[i]
        else:
            x-=1
    if currentDirection == Direction.RIGHT:
        if x == len(grid[y]) - 1:
            for i in range(0, len(grid)):
                grid[i] = grid[i] + ['.']
        x+=1
    if currentDirection == Direction.UP:
        if y == 0:
            grid = [list('.' * len(grid[0]))] + grid
        else:
            y-=1
    return ((x, y), grid)


def solve(grid):
    (x, y) = (int(len(grid[0])/2), int(len(grid)/2))
    facing =  Direction.UP
    infections = 0
    for i in range(0,10000):
        if grid[y][x] == "#":
            grid[y][x] = "."
            facing = turn(facing, Direction.RIGHT)
        elif grid[y][x] == ".":
            grid[y][x] = "#"
            infections += 1
            facing =  turn(facing, Direction.LEFT)
        ((x,y), grid) = move(facing, x, y, grid)
    print_grid(grid, x,y)
    print(infections)

def reverse(direction):
    if direction == Direction.UP:
        return Direction.DOWN
    if direction == Direction.DOWN: 
        return Direction.UP
    if direction == Direction.LEFT:
        return Direction.RIGHT
    if direction == Direction.RIGHT:
        return Direction.LEFT

def solve2(grid):
    (x, y) = (int(len(grid[0])/2), int(len(grid)/2))
    facing =  Direction.UP
    infections = 0
    for i in range(0,10000000):
        if grid[y][x] == "#":
            grid[y][x] = "F"
            facing = turn(facing, Direction.RIGHT)
        # weakened
        elif grid[y][x] == "W":
            grid[y][x] = "#"
            infections += 1
        #flagged
        elif grid[y][x] == "F":
            facing = reverse(facing)
            grid[y][x] = "."
        elif grid[y][x] == ".":
            grid[y][x] = "W"
            facing =  turn(facing, Direction.LEFT)
        ((x,y), grid) = move(facing, x, y, grid)
    print_grid(grid, x,y)
    print(infections)

if __name__ == "__main__":
    grid = load_grid("day22-test.txt")
    solve2(grid)
