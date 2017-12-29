import functools 

def get_sublist(l, start_pos, length):
    end_pos = min(start_pos + length, len(l))
    if end_pos == start_pos + length:
        return l[start_pos:end_pos]
    else:
        diff = abs((start_pos + length) - end_pos)
        return l[start_pos:end_pos] + l[:diff]

def replace_sublist(l, start_pos, length, sublist):
    for i in range(0, length):
        l_index =  (start_pos + i) % len(l)
        l[l_index] = sublist[i]
    return l



def solve(knots):
    l = list(range(0, 256))
    current_pos = 0
    skip_size = 0
    for i in knots:
        sublist = get_sublist(l, current_pos, i)
        sublist.reverse()
        l = replace_sublist(l, current_pos, i, sublist)
        current_pos += i + skip_size 
        current_pos %= len(l)
        skip_size += 1
    print(l[0] * l[1])

    
def solve2(knots):
    knots = list(map(lambda x: ord(x), knots)) 
    knots += [17, 31, 73, 47, 23]
    current_pos = 0
    skip_size = 0
    l = list(range(0, 256))

    for i  in range(0, 64):
        for i in knots:
            sublist = get_sublist(l, current_pos, i)
            sublist.reverse()
            l = replace_sublist(l, current_pos, i, sublist)
            current_pos += i + skip_size 
            current_pos %= len(l)
            skip_size += 1

    dense_hash = []
    for i in range(0, 256, 16):
        dense_hash.append(functools.reduce(lambda x,y : x^y, l[i:i+16]))
    hexcode = ""
    for i in dense_hash:
        h = hex(i)[2:]
        if len(h) == 1:
            h = "0" + h
        hexcode += h
    return hexcode

if __name__ == "__main__":
    solve2("183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88")
    solve([183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88])
