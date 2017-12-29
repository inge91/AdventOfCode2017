import day10


def solve(key):
    s = 0
    for i in range(0, 128):
        current_key = key + "-" + str(i)
        code = day10.solve2(current_key)
        for h in code:
            b = bin(int(h, 16))[2:]
            b_list = [int(x) for x in str(b)]
            s += sum(b_list)
    print(s)


def get_neighbours(i, j, l):
    neighbours = []
    if i > 0:
        neighbours.append((i - 1, j))
    if j > 0:
        neighbours.append((i, j - 1))
    if i < 127:
        neighbours.append((i + 1, j))
    if j < 127:
        neighbours.append((i, j + 1))
    return neighbours

def flood(i, j, l, v):
    to_flood = [(i, j)]
    while len(to_flood) > 0:
        e = to_flood[0]
        to_flood = to_flood[1:]
        if l[e[0]][e[1]] is not "1":
            continue

        l[e[0]][e[1]] = v

        neighbours = get_neighbours(e[0], e[1], l)
        for n in neighbours:
            to_flood.append(n)
    return l


def solve2(key):
    s = 0
    lines = []
    for i in range(0, 128):
        current_key = key + "-" + str(i)
        code = day10.solve2(current_key)
        b_combined = ""
        for h in code:
            b = bin(int(h, 16))[2:]
            while len(b) < 4:
                b = "0" + b 
            b_combined += b
        lines.append(list(b_combined))
    
    region_no = 2
    for i in range(0, 128):
        for j in range(0, 128):
            if lines[i][j] is not "1":
                continue
            else:
                lines = flood(i, j, lines, region_no)
                region_no += 1
    print(region_no-2)
            

if __name__ == "__main__":
    solve2("hxtvlmkl")
    solve("hxtvlmkl")
