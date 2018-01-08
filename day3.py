
def update(x, y, grid):
    s = 0
    s += grid[y][x-1]
    s += grid[y][x+1]
    s += grid[y+1][x-1]
    s += grid[y+1][x+1]
    s += grid[y+1][x]
    s += grid[y-1][x]
    s += grid[y-1][x-1]
    s += grid[y-1][x+1]
    grid[y][x] = s
    return grid


def printgrid(grid):
    for row in grid:
        print(row)

def generate():
    grid = [[0 for x in range(20)] for y in range(20)]
    x = 10
    y = 10
    grid[y][x] = 1
    x += 1
    while True:
        for i in range (0)
        i = input()
        if i == "w":
            y -= 1
        if i == "s":
            y += 1
        if i == "a":
            x -= 1
        if i == "d":
            x += 1
        grid = update(x, y, grid)
        printgrid(grid)

def solve():
    generate()


if __name__ == "__main__":
    solve()
