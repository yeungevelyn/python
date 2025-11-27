from datastructure.stack.Node import Node


class MyStack:#{
    """
    Implementation of a LIFO Stack as a linked list
    that connect topNode -> node -> node -> … -> NULL
    """
    def __init__(self):#{
        """
        Constructs an empty stack
        """
        self.topNode = None
    #}

    def top(self): # {
        """
        Returns the item stored at the top of the stack,
        but do not remove it.
        If the stack is empty then returns None.
        """
        if self.topNode == None:
            return None
        return self.topNode.datum
    # }

    def push(self, item): # {
        """
        Adds an item to the top of the stack
        """
        # create a new node to be put at the top of the stack
        newNode = Node(datum=item, next=None)
        if self.topNode == None:
            # stack is empty
            self.topNode = newNode
        else:
            newNode.next = self.topNode
            self.topNode = newNode
    # }

    def pop(self): # {
        """
        Removes the item stored at the top of the stack and returns it.
        If the stack is empty then returns None.
        """
        # if the stack is empty
        if (self.topNode == None):
            return None
        # get the item stored at the top node
        item = self.topNode.datum
        # reset the top node of this stack
        self.topNode = self.topNode.next
        return item
    # }
#}

#Main program
# testing stack
stackObj = MyStack()
# push() add item to the stack
stackObj.push("dog")
stackObj.push("cat")
stackObj.push("frog")
# top() get top item of the stack, but do not remove it
print("using top():")
print(stackObj.top())
print(stackObj.top())
print(stackObj.top())
# pop() remove item from stack in LIFO order
print("using pop():")
print(stackObj.pop())
print(stackObj.pop())
print(stackObj.pop())
print(stackObj.pop())