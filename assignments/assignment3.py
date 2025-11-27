#get user input
int1 = input("Enter 1st integer: ")
int2 = input("Enter 2nd integer: ")
word = input("Enter a word: ")
option = input("Enter display option (A/B): ")
#print output
for i in range(int(int1),int(int2)+1):
    result = i*10
    if (option == "A"):
        print("{}: {} x {} ={}".format(word,i,10,result))
    else:
        print("{} x {} ={} :{}".format(i,10,result,word))


# question2
# print("A blue number is a positive integer")
# print("that ends with 7, such as 6127.")
# print("Keep asking user until Q for quit.")
# print()
# #get user input
# while True:
#     numb = input("Enter a number: ")
#     #if user input Q, quit
#     if(numb == "Q"):
#         print("Good bye!")
#         break
#     num_int = int(numb)
#     #determine number whether is blue
#     # get end number of numb
#     last_num = numb[len(numb)-1]
#     if (num_int>0 and last_num=="7"):
#         print("This number {} is blue".format(numb))
#     else:
#         print("This number {} is NOT blue".format(numb))











# please modify the following given code for the function
# do not include the test cases
def insertionSort(intList):
#{
    print("Start insertion sort for {}".format(intList))
    n = len(intList)
    print("List length: {}".format(n))
    for i in range(1, n):
    #{
        print("i={}".format(i))
        # sort intList[0], intList[1], ..., intList[i]
        k = i
        while (k > 0) and (intList[k-1] > intList[k]):
        #{
            # swap intList[k] and intList[k-1]
            print("swap intList[{}] and intList[{}]".format(k,k-1))
            temp = intList[k]
            intList[k] = intList[k-1]
            intList[k-1] = temp
            print("list becomes {}".format(intList))

            k = k - 1
        #}
    #}
#}

# insertionSort(intList=[60, 10, 90, 50, 100, 80])