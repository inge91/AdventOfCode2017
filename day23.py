def getValue(val, program_vars):
    try:
        return int(val)
    except ValueError:
        return program_vars[val]

def setValue(var, val, program_vars):
    program_vars[var] = val

def solve(instructions):
    program = {"a" : 1, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0}
    currentInstruction = 0
    mulCall = 0
    while currentInstruction < len(instructions):
        print(instructions[currentInstruction])
        print("a {} b {} c {} d {} e {} f {} g {} h {}".format(program["a"],program["b"],program["c"],program["d"],program["e"],program["f"],program["g"],program["h"]))
        print(currentInstruction)
        _ = input("")
        (offset, mul) = performInstruction(program, instructions[currentInstruction])
        currentInstruction += offset
        mulCall += mul
    print(mulCall)

def performInstruction(variables, instruction):
    offset = 1
    operation = instruction[0]
    register = instruction[1] # register can also be just a value.
    mul = 0
    if operation == "set":
        val = getValue(instruction[2], variables)
        setValue(register, val, variables)
    if operation == "add":
        val = getValue(instruction[2], variables)
        setValue(register, getValue(register, variables) + val, variables)
    if operation == "mul":
        val = getValue(instruction[2], variables)
        setValue(register, getValue(register, variables) * val, variables)
        mul = 1
    if operation == "sub":
        val = getValue(instruction[2], variables)
        setValue(register, getValue(register, variables) - val, variables)
    if operation == "mod":
        val = getValue(instruction[2], variables)
        setValue(register, getValue(register, variables) % val, variables)
    if operation == "jnz" : 
        if getValue(register, variables) != 0:
            offset = getValue(instruction[2], variables)
    return (offset, mul)


def getInstructions(f):
    instruction_list = []
    instructions = open(f)
    for instruction in instructions:
        instruction = instruction.rstrip("\n")
        l = instruction.split(" ")
        instruction_list.append(l)
    return instruction_list

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# This solution was found by first 
# rewriting the instructions to python
# code. Then I realized that h is incremented
# when the iterator b wasn't prime, since 
# { h++ | {e,d}  range(2, b) x range(2, b) && e * d == b}
def solve2():
    b = 109300
    c = 126300
    h = 0
    while True:
        if not isPrime(b):
            h += 1 
        if b == c:
            print(h)
            break
        b += 17

if __name__ == "__main__":
    instructions = getInstructions("day23.txt")
    solve(instructions)
