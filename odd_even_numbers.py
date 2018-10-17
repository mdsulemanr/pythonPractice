def numTest(num):
    evenNum = []
    oddNum = []
    for i in num:
        if i % 2 == 0:
            evenNum.append(i)
        else:
            oddNum.append(i)
    return evenNum, oddNum


num = [x for x in range(0, 101)]

print(numTest(num))


def counDown():
    counting = []
    (evenNum, oddNum) = numTest(num)
    result = list(zip(evenNum, oddNum))
    for i, j in result:
        counting+=i,j

    return counting


print(counDown())