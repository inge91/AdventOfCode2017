
def parseInput(f):
    steps = [int(line.rstrip('\n')) for line in open(f)]
    return steps


def solve(steps):
    i = 0
    count = 0
    while i < len(steps):
        offset = steps[i]
        steps[i] += 1
        i += offset
        count += 1
    print(count)
    return count

def solve2(steps):
    i = 0
    count = 0
    while i < len(steps):
        offset = steps[i]
        if offset >= 3:
            steps[i] -= 1
        else:
            steps[i] += 1
        i += offset
        count += 1
    print(count)
    return count


if __name__ == "__main__":
    steps = parseInput("day5.txt")
    solve2(steps)
