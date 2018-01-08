import queue 
import copy

def parseInput(f):
    pipes = open(f)
    pipes_list = []
    for pipe in pipes:
        p1, p2 = pipe.rstrip("\n").split("/")
        pipes_list.append((int(p1), int(p2)))
    return pipes_list

def last_element(bridge):
    p1, p2 = bridge[-1]
    if p1 == 0 or p1 in bridge[-2]:
        return p2
    return p1

def get_expansions(bridge, pipes):
    element = last_element(bridge)
    expansion_elements = []
    for pipe in pipes:
        if element in pipe and pipe not in bridge:
            expansion_elements.append(pipe)
    return expansion_elements

def solve(pipes):
    finished_bridges = []
    bridges = queue.Queue()
    bridges.put([(0, 0)])
    while bridges.qsize() > 0:
        bridge = bridges.get()
        elements = get_expansions(bridge, pipes)
        if len(elements) == 0:
            finished_bridges.append(bridge)
        else:
            for element in elements:
                new_bridge = copy.copy(bridge)
                new_bridge.append(element)
                bridges.put(new_bridge)
    bridge_sums = []
    for bridge in finished_bridges:
        bridge_sums.append(sum([sum(x) for x in bridge]))
    print("max bridge sum: {}".format(max(bridge_sums)))
    finished_bridges.sort(key = lambda x:len(x))
    max_len = len(finished_bridges[-1])
    max_len_bridges = [x for x in finished_bridges if len(x) == max_len]
    bridge_sums = []
    for max_len_bridge in max_len_bridges:
        bridge_sums.append(sum([sum(x) for x in max_len_bridge]))
    print("bridge with max length and sum: {}".format(max(bridge_sums)))



if __name__ == "__main__":
    pipes =  parseInput("day24.txt")
    solve(pipes)
