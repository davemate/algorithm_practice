def getBit(number, i):
    num = 1 << i
    return ((num) & number) != 0


def setBit(number, i):
    num = 1 << i
    return num | number


def updateBit(number, bit, i):
    bitMask = 1 << i
    bitMask = ~bitMask
    return (number & bitMask) | (bit << i)


def clearBit(number, i):
    bitMask = 1 << i
    bitMask = ~bitMask
    return number & bitMask


print(getBit(1, 1))
print(setBit(4, 2))
print(updateBit(4, 0, 2))
print(clearBit(4, 2))


#5.1