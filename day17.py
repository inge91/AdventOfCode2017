
def solve(steps):
    buf = [0]
    currentPos = 0
    for currentInsert in range(1, 2018):
       currentPos += steps 
       currentPos %=  len(buf)
       currentPos += 1
       buf.insert(currentPos, currentInsert)
    print(buf[currentPos+1])


#insight for part 2: We don't actually have to
# keep the state of the buffer, we just have to
# know at what point we insert a new value at
# index 1 of the buffer. This saves computation time.
def solve2(steps):
    buf = 1
    currentPos = 0
    secondValue = 0
    for currentInsert in range(1, 50000000):
       currentPos += steps
       currentPos %=  buf
       currentPos += 1
       if currentPos == 1:
           secondValue = currentInsert
       buf += 1
    print(secondValue)


if __name__ == "__main__":
    solve2(324)
