def selectionSort(intList):
    n = len(intList)
    for i in range(0, n-1):
    #{
        # find the minimum item in intList[i .. n-1]
        kMin = i
        for k in range(i+1, n):
            if (intList[k] < intList[kMin]):
                kMin = k
        # swap intList[i] and intList[kMin]
        if (kMin != i):
            temp = intList[i]
            intList[i] = intList[kMin]
            intList[kMin] = temp
    #}