

def solve(a, b):
    matches = 0
    divider = 2147483647
    for i in range(0, 40000000):
        a *= 16807
        b *= 48271
        a %= divider
        b %= divider
        a_bin = bin(a)[-16:]
        b_bin = bin(b)[-16:]
        if a_bin == b_bin:
            matches += 1
    print(matches)
    

def solve2(a, b):
    matches = 0
    divider = 2147483647
    for i in range(0, 5000000):
        a *= 16807
        a %= divider
        while a % 4 != 0:
            a *= 16807
            a %= divider

        b *= 48271
        b %= divider
       
        while b % 8 != 0:
            b *= 48271
            b %= divider

        a_bin = bin(a)[-16:]
        b_bin = bin(b)[-16:]
        if a_bin == b_bin:
            matches += 1
    print(matches)
    

if __name__ == "__main__":
    solve2(289, 629)
