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


def solve(layers):
    l = []
    for layer in layers:
        l.append(Layer(layer[0], layer[1]))

    severity = 0

    current_pos = 0
    while current_pos < 98:
        severity += calculate_severity(l, current_pos)
        for layer in l:
            layer.update_scanner_pos()
        current_pos += 1

    print(severity)
        

def wait(l, picoseconds_to_wait):
    for i in range(0, picoseconds_to_wait):
        for layer in l:
            layer.update_scanner_pos()

def solve2(layers):
    l = []
    for layer in layers:
        l.append(Layer(layer[0], layer[1]))

    picoseconds_waited = 0
    while True: 
        l2 = copy.deepcopy(l)
        wait(l2, picoseconds_waited)
        current_pos = 0
        severity = 0
        while current_pos <= 98:
           # print("pos")
           # print(current_pos)
           # print("layers")
           # for layer in l2:
           #     print(layer.scanner_pos)
            (is_hit, hit_severity) = calculate_severity(l2, current_pos)
            if is_hit:
                severity += hit_severity
                break
            for layer in l2:
                layer.update_scanner_pos()
            current_pos += 1
        if not is_hit:
            print(picoseconds_waited)
            break
        picoseconds_waited += 1
        



if __name__ == "__main__":
    solve2(
[[0, 3],
[1, 2],
[2, 4],
[4, 4],
[6, 5],
[8, 6],
[10, 8],
[12, 8],
[14, 6],
[16, 6],
[18, 8],
[20, 8],
[22, 6],
[24, 12],
[26, 9],
[28, 12],
[30, 8],
[32, 14],
[34, 12],
[36, 8],
[38, 14],
[40, 12],
[42, 12],
[44, 12],
[46, 14],
[48, 12],
[50, 14],
[52, 12],
[54, 10],
[56, 14],
[58, 12],
[60, 14],
[62, 14],
[66, 10],
[68, 14],
[74, 14],
[76, 12],
[78, 14],
[80, 20],
[86, 18],
[92, 14],
[94, 20],
[96, 18],
[98, 17]])


