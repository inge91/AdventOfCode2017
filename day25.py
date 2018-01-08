from enum import Enum

class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5

def createInstructions():
    action = {}
    action[(State.A, 0)] = (1, 1, State.B)
    action[(State.A, 1)] = (0, 1, State.C)

    action[(State.B, 0)] = (0, -1, State.A)
    action[(State.B, 1)] = (0, 1, State.D)

    action[(State.C, 0)] = (1, 1, State.D)
    action[(State.C, 1)] = (1, 1, State.A)

    action[(State.D, 0)] = (1, -1, State.E)
    action[(State.D, 1)] = (0, -1, State.D)

    action[(State.E, 0)] = (1, 1, State.F)
    action[(State.E, 1)] = (1, -1, State.B)

    action[(State.F, 0)] = (1, 1, State.A)
    action[(State.F, 1)] = (1, 1, State.E)
    return action

def solve():
    tape = [0] * 15000000
    i = 500000
    actions = createInstructions()
    state = State.A
    for _ in range(12368930):
        (val, offset, state) = actions[(state, tape[i])]
        tape[i] = val
        i += offset
        if i < 0:
            tape = [0] + tape
        if i >= len(tape):
            tape += [0]
    print(sum(tape))




if __name__ == "__main__":
    solve()
