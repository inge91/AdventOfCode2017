import copy

def horizontal_flip(sub_square):
    tmp = copy.copy(sub_square)
    for i in range(0, len(tmp)):
        l = list(tmp[i])
        l.reverse()
        tmp[i] = "".join(l)
    return tmp

def vertical_flip(sub_square):
    tmp = copy.copy(sub_square)
    tmp_line = tmp[0]
    tmp[0] = tmp[-1]
    tmp[-1] = tmp_line
    return tmp

def rotate(sub_square):
    tmp = copy.copy(sub_square)
    for y in range(0, len(sub_square)):
        for x in range(0, len(sub_square)):
            tmp[y] = tmp[y][:x] + sub_square[x][len(sub_square)-1-y] + tmp[y][x+1:] 
    return tmp

def getPermutations(sub_square):
    permutations = []
    for i in range(0, 4):
        permutations.append(sub_square)
        permutations.append(horizontal_flip(sub_square))
        permutations.append(vertical_flip(sub_square))
        sub_square = rotate(sub_square)
    return permutations

def print_square(square):
    square = square.split("/")
    for line in square:
        print(line)
    print("\n")

def solve(square, rules):
    for i in range(0, 18):
        print(i)
        size = square.find("/")
        rows = square.split("/")

        # deconstruct squares
        if size % 2 == 0:
            modifier = 2
        elif size % 3 == 0:
            modifier = 3
        sub_squares = []
        for y in range(0, size, modifier):
            for x in range(0, size, modifier):
                sub_squares.append("")
                sub_squares[-1] += rows[y][x:x+modifier]
                sub_squares[-1] += "/"
                sub_squares[-1] += rows[y+1][x:x+modifier]
                if modifier == 3:
                    sub_squares[-1] += "/"
                    sub_squares[-1] += rows[y+2][x:x+modifier]

        # Apply rules
        new_squares = []
        for sub_square in sub_squares:
            sq = rules[sub_square]
            sq = sq.split("/")
            new_squares.append(sq)

        # append new squares
        new_square =  ""
        for sq in new_squares:
            sq = "/".join(sq)
        for i in range(0, len(new_squares), int(size/modifier)):
            for j in range(0, len(new_squares[0])):
                for k in range(i, i + int(size/modifier)):
                    new_square += new_squares[k][j]
                new_square += "/"
        square = new_square
    print(square.count("#"))

def makeRules(f):
    d = {}
    rules = open(f)
    for rule in rules:
        (rule_in, rule_out) = rule.split(" => ")
        rule_in_list = rule_in.split("/")
        perms = getPermutations(rule_in_list)
        for perm in perms:
            perm = "/".join(perm)
            if perm not in d.keys():
                d[perm] = rule_out[:-1]
    return d

if __name__ == "__main__":
    rules = makeRules("day21.txt")
    solve(".#./..#/###", rules)
    

