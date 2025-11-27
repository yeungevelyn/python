from queue import Queue
count = int(input("Enter person count: "))
# initial the queue to hold [1, 2, 3, ..., count]
queue = Queue()
for i in range(1, count+1):
    queue.put(i)
while True:
    # person at the front of the queue has the turn to kill the next person
    person_get_turn = queue.get()
    person_get_killed = queue.get()
    print("{0} kills {1}".format(person_get_turn, person_get_killed))
    if queue.empty():
        print("{0} is the last person".format(person_get_turn))
        break
    # append person_get_turn to the end of the Queue
    queue.put(person_get_turn)