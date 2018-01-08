from enum import Enum
import copy

class Direction(Enum):
    UP=1
    DOWN=2

class Layer:
    def __init__(self, index, r):
        self.max_range = r
        self.index = index
        self.direction = Direction.DOWN
        self.scanner_pos = 1

    def printState(self):
        for i in range(self.max_range):
            if(self.scanner_pos - 1 == i):
                print("S ", end='')
            else:
                print("_ ", end='')
        print()
            

    def update_scanner_pos(self):
        if self.direction == Direction.DOWN:
            if self.scanner_pos < self.max_range:
                self.scanner_pos += 1
            else:
                self.direction = Direction.UP
                self.scanner_pos -= 1
        else:
            if self.scanner_pos > 1:
                self.scanner_pos -= 1
            else:
                self.direction = Direction.DOWN
                self.scanner_pos += 1

def calculate_severity(layers, pos):
    for layer in layers:
        if pos == layer.index and layer.scanner_pos == 1:
            return (True, layer.max_range * layer.index)
    return (False, 0)



def wait(l, picoseconds_to_wait, verbose = False):
    for i in range(0, picoseconds_to_wait):
        for layer in l:
            layer.update_scanner_pos()
        if verbose:
            print_state(l, 0)

def print_state(l, pos):
    i = 0
    count = 0
    while i <= l[-1].index:
        if i < l[count].index:
            if pos == i:
                print("x")
            else:
                print(".")
        else:
            if pos == i:
                print("x", end="")
            l[count].printState()
            count += 1
        i+=1
    print()

def solve(l, picoseconds_waited = 0, verbose = False):
    wall_size = l[-1].index
    severity = 0
    current_pos = 0
    wait(l, picoseconds_waited, False)
    been_hit = False
    while current_pos <= wall_size:
        hit, hit_severity = calculate_severity(l, current_pos)
        if verbose:
            print_state(l, current_pos)
        if not been_hit and hit:
            been_hit = True
        severity += hit_severity
        for layer in l:
            layer.update_scanner_pos()
        current_pos += 1
    if verbose:
        print_state(l, current_pos)
    return been_hit, severity
        
def hit(l, wait):
    for layer in l:
        steps = (layer.max_range-1) * 2
        if (layer.index + wait) % steps == 0:
            return True
    return False 

def solve3(l):
    picoseconds_waited = 0
    while True:
        if hit(l, picoseconds_waited):
            picoseconds_waited += 1
        else:
            #solve(l, picoseconds_waited, True)
            print("Solved: ")
            print(picoseconds_waited)
            break

def parseInput(f):
    layer_list = []
    layers = open(f)
    for layer in layers:
        layer = layer.rstrip("\n").split(": ")
        layer_list.append(Layer(int(layer[0]), int(layer[1])))
    return layer_list 

if __name__ == "__main__":
    layers = parseInput("day13.txt")
    solve3(layers)

