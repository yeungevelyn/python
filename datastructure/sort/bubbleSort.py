"""
for - loop n-1
every for loop is from 1st number to n-i item,
coz the biggest number will be put on the last.
every loop will add a new ordered number in the last.
"""
def bubbleSort(intList):
    n = len(intList)
    for i in range(0, n-1):
    #{
        for j in range(1, n-i):
        #{
            # compare adj items, swap if in wrong order
            if intList[j-1] > intList[j]:
                # swap intList[j-1] and intList[j]
                temp = intList[j-1]
                intList[j-1] = intList[j]
                intList[j] = temp
        #}
    #}


"""
advanced bubbl sort
"""
def bubbleSort(intList):
    n = len(intList)
    for i in range(0, n-1):
        swapped = False
        for j in range(1, n-i):
            # compare adj items, swap if in wrong order
            if intList[j-1] > intList[j]:
                # swap intList[j-1] and intList[j]
                temp = intList[j-1]
                intList[j-1] = intList[j]
                intList[j] = temp
             # remember that swap is needed
                swapped = True
        if not swapped:
            # swap is NOT needed, so list is SORTED
            break

"""
practice
"""


def bubble_sort(self, sort_list):
    n = len(sort_list) - 1
    for i in range(0, n):
        for j in range(0, n - i):
            # compare  numbers, swap if they're in wrong order
            if sort_list[j] > sort_list[j + 1]:
                temp = sort_list[j]
                sort_list[j] = sort_list[j + 1]
                sort_list[j + 1] = temp