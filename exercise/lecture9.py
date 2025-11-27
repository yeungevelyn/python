import random
animal_list = ["dog", "cat", "frog"]
# for animal in animal_list:
#     print(animal)
# for i in range (0,len(animal_list)):
#     print(animal_list[i])

# index = random.randint(0,len(animal_list)-1)
# print(index)
# print(animal_list[index])

fibo_numbers = [0, 1, 1, 2, 3, 5, 8, 13]

# write code here to add the following numbers
# 21, 34 and 55 to the end of the list
fibo_numbers.append(21)
fibo_numbers.append(34)
fibo_numbers.append(55)
# print(fibo_numbers)

random_numbers = [1, 4, 4, 10, -1]

# write code using for-loop to
# increase each number in the list by 20

for i in range(0,len(random_numbers)):
    #calculate
    new_number = random_numbers[i]+20
    random_numbers[i] = new_number


# Create a list called square_list and use a for-loop to put the 10 square numbers 1, 4, 9, ..., 100 into the list.
square_list=[]
for i in range (1,11):
    #get square
    item = i*i
    #put in list
    square_list.append(item)

def doubling(list):
    # write your code here
    repeated_list =[]
    #get item in list
    for item in list:
        repeated_list.append(item)
        repeated_list.append(item)
    return repeated_list
# a_list=[4,5,6]
# repeated_list = doubling(a_list)
# print(repeated_list)

def list_multiply(list1, list2):
  # write your code here
    list3=[]
    for i in range (0,len(list1)):
        #calculate
        item = list1[i]*list2[i]
        list3.append(item)
    return list3

# result = list_multiply([4,5,6],[10,0,1])
# print(result)

from queue import LifoQueue
# creating a stack
stack = LifoQueue()
# add 3 items
stack.add("aaa")
stack.add("bbb")
stack.add("ccc")

from queue import Queue
#creating a queue
queue = Queue()
# add item
queue.put("aaa")
queue.put("bbb")
queue.put("ccc")