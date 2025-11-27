import Node
class LinkedList: #{
    """
    Implements of a linked list data structure
    that connect firstNode -> node1 -> node2 -> node3
    """
    def __init__(self):
        """
        Constructs an empty LinkedList
        """
        self.firstNode = None

    def insertFirst(self, datum):
        """
        Inserts a new node at the beginning of the list
        :param datum:
        :return:
        """

        #create a new node
        newNode = Node.Node(datum=datum, next=self.firstNode)
        #set the new node to be the first node of the list
        self.firstNode = newNode

    def removeFirst(self):
        """
        Removes the first node from the list
        :return: None if the list is empty, otherwise the removed node and return the removed node
        """
        #if list is empty
        if (self.firstNode == None):
            return None
        #get first datum
        firstDatum = self.firstNode.datum
        #remove the first node
        self.firstNode = self.firstNode.next
        return firstDatum

#}

    #MAIN Program
llobj = LinkedList()
llobj.insertFirst("cat")
llobj.insertFirst("dog")
llobj.insertFirst("emu")
llobj.removeFirst()
print(llobj)
