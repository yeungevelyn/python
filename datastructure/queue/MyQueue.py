from datastructure.queue.Node import Node


class MyQueue: #{
    """
    Implementation of a FIFO Queue as a linked list
    that connect frontNode -> node -> node -> ... -> endNode -> NULL
    """
    def __init__(self): #{
        """
        Constructs an empty queue
        """
        self.frontNode = None
        self.endNode = None
    #}

    def front(self): # {
        """
        Returns the item stored at the front of the queue,
        but do not remove it.
        If the queue is empty then returns None.
        """
        if self.frontNode == None:
            return None
        return self.frontNode.datum
    # }

    def enqueue(self, item): #{
        """
        Adds an item to the end of the queue
        """
        # create a new node to be put at the end of the queue
        newNode = Node(datum=item, next= None)
        if self.frontNode == None:
            # queue is empty
            self.frontNode = newNode
            self.endNode = newNode
        else:
            self.endNode.next = newNode
            self.endNode = newNode
    #}


    def dequeue(self): #{
        """
        Removes the item stored at the front of the queue and return it.
        If the queue is empty then returns None.
        """
        # if the queue is empty
        if (self.frontNode == None):
            return None
        # get the item stored at the front node
        item = self.frontNode.datum
        # reset the front    node of this queue
        self.frontNode = self.frontNode.next
        # if the queue becomes empty
        if (self.frontNode == None):
            self.endNode = None
        return item
    #}
#}

#main program
# testing queue
queueObj = MyQueue()
# enqueue() add item to the queue
queueObj.enqueue("dog")
queueObj.enqueue("cat")
queueObj.enqueue("frog")
# front() get front item of the queue, but do not remove it
print("using front():")
print(queueObj.front())
print(queueObj.front())
print(queueObj.front())
# dequeue() remove item from queue in FIFO order
print("using dequeue():")
print(queueObj.dequeue())
print(queueObj.dequeue())
print(queueObj.dequeue())
print(queueObj.dequeue())