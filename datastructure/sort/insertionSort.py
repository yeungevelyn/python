def insertionSort(intList):
    n = len(intList)
    for i in range(1, n):
    #{
        # sort intList[0], intList[1], ..., intList[i]
        k = i
        while (k > 0) and (intList[k-1] > intList[k]):
        #{
            # swap intList[k] and intList[k-1]
            temp = intList[k]
            intList[k] = intList[k-1]
            intList[k-1] = temp
            k = k - 1
        #}
    #}