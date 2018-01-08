def getValue(val, program_vars):
    try:
        return int(val)
    except ValueError:
        return program_vars[val]

def setValue(var, val, program_vars):
    program_vars[var] = val

def solve(instructions):
    last_sound_frq = 0
    step = 0
    while step < len(instructions):
        instruction = instructions[step]
        operation = instruction[0]
        register = instruction[1] # register can also be just a value.
        #print(instruction)
        #print("a {} b {} p {} i {} f {}".format(a,b,p,i,f))
        performedJump = False
        if operation == "set":
            val = getValue(instruction[2])
            setValue(register, val)
        if operation == "snd":
            val = getValue(register)
            print("Played sound in register {0} with freq {1}".format(register,
                    val))
            last_sound_frq = val
        if operation == "add":
            val = getValue(instruction[2])
            setValue(register, getValue(register) + val)
        if operation == "mul":
            val = getValue(instruction[2])
            setValue(register, getValue(register) * val)
        if operation == "mod":
            val = getValue(instruction[2])
            setValue(register, getValue(register) % val)
        if operation == "rcv":
            val = getValue(register)
            if val != 0:
                print("Recovered sound with frequency: {}".format(last_sound_frq))
                return
        if operation == "jgz" : 
            offset = getValue(instruction[2])
            if getValue(register) > 0:
                step += offset
                performedJump = True
        if not performedJump:
            step += 1


def performInstruction(variables, instruction, readbuf, writebuf):
    offset = 1
    operation = instruction[0]
    register = instruction[1] # register can also be just a value.
    sendVal = False
    if operation == "set":
        val = getValue(instruction[2], variables)
        setValue(register, val, variables)
    if operation == "snd":
        val = getValue(register, variables)
        writebuf.append(val)
        sendVal = True
    if operation == "add":
        val = getValue(instruction[2], variables)
        setValue(register, getValue(register, variables) + val, variables)
    if operation == "mul":
        val = getValue(instruction[2], variables)
        setValue(register, getValue(register, variables) * val, variables)
    if operation == "mod":
        val = getValue(instruction[2], variables)
        setValue(register, getValue(register, variables) % val, variables)
    if operation == "rcv":
        if len(readbuf) == 0:
            offset = 0
        else:
            setValue(register, readbuf[0], variables)
            del readbuf[0]
    if operation == "jgz" : 
        if getValue(register, variables) > 0:
            offset = getValue(instruction[2], variables)
    return (offset, sendVal)

def solve2(instructions):
    program1 = {"a" : 0, "b" : 0, "p" : 0, "i" : 0, "f" : 0}
    program2 = {"a" : 0, "b" : 0, "p" : 1, "i" : 0, "f" : 0}
    step1 = 0
    step2 = 0
    sendCount = 0
    buffer1 = [] #program 2 writes to buffer1, program1 reads from it
    buffer2 = [] #program 1 writes to buffer1, program 2 reads from it
    while step1 < len(instructions) and step2 < len(instructions):
        instruction1 = instructions[step1]
        instruction2 = instructions[step2]
        (offset1, _) = performInstruction(program1, instruction1, buffer1, buffer2)
        (offset2, sendVal) = performInstruction(program2, instruction2, buffer2, buffer1)
        if sendVal:
            sendCount += 1
        step1 += offset1
        step2 += offset2
        if offset1 == 0 and offset2 == 0:
            print("Dead lock Reached. Terminating")
            break
    print(sendCount)

if __name__ == "__main__":
    solve2(
#[["snd",1],
#["snd",2],
#["snd","p"],
#["rcv","a"],
#["rcv","b"],
#["rcv","c"],
#["rcv","d"]])
[["set", "i", 31],
["set", "a", 1],
["mul", "p", 17],
["jgz", "p", "p"],
["mul", "a", 2],
["add", "i", -1],
["jgz", "i", -2],
["add", "a", -1],
["set", "i", 127],
["set", "p", 316],
["mul", "p", 8505],
["mod", "p", "a"],
["mul", "p", 129749],
["add", "p", 12345],
["mod", "p", "a"],
["set", "b", "p"],
["mod", "b", 10000],
["snd", "b"],
["add", "i", -1],
["jgz", "i", -9],
["jgz", "a", 3],
["rcv", "b"],
["jgz", "b", -1],
["set", "f", 0],
["set", "i", 126],
["rcv", "a"],
["rcv", "b"],
["set", "p", "a"],
["mul", "p", -1],
["add", "p", "b"],
["jgz", "p", 4],
["snd", "a"],
["set", "a", "b"],
["jgz", 1, 3],
["snd", "b"],
["set", "f", 1],
["add", "i", -1],
["jgz", "i", -11],
["snd", "a"],
["jgz", "f", -16],
["jgz", "a", -19]])

