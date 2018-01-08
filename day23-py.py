
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solve():
    b = 109300
    c = 126300
    h = 0
    while True:
        f = 1
        if not isPrime(b):
            h += 1 
            print(h)
        if b == c:
            print(h)
            break
        b += 17

if __name__ == "__main__":
    solve()
    
    




