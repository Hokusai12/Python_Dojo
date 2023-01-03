def countdown(num):
    newList = []
    for i in range(num, -1, -1):
        newList.append(i)
    return newList

print(countdown(21))


def printAndReturn(list):
    print(list[0])
    return list[1]

print(printAndReturn([0, 4]))


def firstPlusLength(list):
    return list[0] + len(list)

print(firstPlusLength([4, 3, 6, 1, 3]))


def valuesGreaterThanSecond(list):
    newList = []
    for i in range(len(list)):
        if list[i] > list[1]:
            newList.append(list[i])
    print(len(newList))
    return newList

print(valuesGreaterThanSecond([5,2,3,2,1,4]))


def thisLengthThatValue(size, value):
    newList = []
    for i in range(size):
        newList.append(value)

    return newList

print(thisLengthThatValue(4, 7))