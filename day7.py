from collections import defaultdict

def parseInput(f):
    flat_tree = {}
    values = {}
    entries = open(f)
    for entry in entries:
        if "->" in entry:
            root, children = entry.split(" -> ")
            root_name, val = root.split(" ")
            flat_tree[root_name] = children.rstrip("\n").split(", ")
        else:
            root = entry.rstrip("\n")
            root_name, val = root.split(" ")
        values[root_name] = int(val[1:-1])
    return flat_tree, values

def getOutlier(values):
    d = defaultdict(int)
    for n, v in values:
        d[v] += 1
    for n, v in values:
        if d[v] == 1:
            return (n, v)

def solve(flat_tree, values, root):
    if root not in flat_tree:
        return values[root]
    children = flat_tree[root]
    child_values = []
    for child in children:
        child_values.append((child, solve(flat_tree, values, child)))
    accum_values = [y for x, y in child_values]
    if len(set(accum_values)) > 1:
        print("Values of children are not the same: ")
        outlier, value = getOutlier(child_values)  
        for v in accum_values:
            if v != value:
                print("answer is: {}".format(abs(values[outlier] + (v-value))))
                accum_values = len(accum_values) * [v]
                break


    return sum(accum_values) + values[root] 

if __name__ == "__main__":
    flat_tree, values = parseInput("day7.txt")
    solve(flat_tree, values, "mkxke")
