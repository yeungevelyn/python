# Implementation of a binary tree
class TreeNode:
#{
    """
    Representing a tree node consisting of
    - datum: the datum stored at the node
    - left: reference to the left child node
    - right: reference to the right child node
    """

    def __init__(self, datum, left, right):
    #{
        self.datum = datum
        self.left = left
        self.right = right
    #}

    def in_order_print(self):
    #{
        """
        Use in-order traversal: left subtree - current node - right subtree,
        and print datum
        """

        # left subtree
        if self.left != None:
            self.left.in_order_print()

        # current node
        print(self.datum)

        # right subtree
        if self.right != None:
            self.right.in_order_print()
    #}

    def pre_order_print(self):
    #{
        """
        Use pre-order traversal: current node - left subtree - right subtree,
        and print datum
        """

        # current node
        print(self.datum)

        # left subtree
        if self.left != None:
            self.left.pre_order_print()

        # right subtree
        if self.right != None:
            self.right.pre_order_print()
    #}

    def post_order_print(self):
    #{
        """
        Use post-order traversal: left subtree - right subtree - current node,
        and print datum
        """

        # left subtree
        if self.left != None:
            self.left.post_order_print()

        # right subtree
        if self.right != None:
            self.right.post_order_print()

        # current node
        print(self.datum)
    #}
#}

class MyBinaryTree:
#{
    """
    Implementation of a binary tree
    """

    def __init__(self):
    #{
        """
        Constructs an empty tree
        """
        self.root = None
    #}

    def print_in_order(self):
    #{
        """
        Use in-order traversal and print each tree node's datum
        """
        if self.root != None:
            self.root.in_order_print()
    #}

    def print_pre_order(self):
    #{
        """
        Use pre-order traversal and print each tree node's datum
        """
        if self.root != None:
            self.root.pre_order_print()
    #}

    def print_post_order(self):
    #{
        """
        Use post-order traversal and print each tree node's datum
        """
        if self.root != None:
            self.root.post_order_print()
    #}

#}

# construct tree node objects
nodeI = TreeNode(datum="I", left=None, right=None)
nodeJ = TreeNode(datum="J", left=None, right=None)
nodeK = TreeNode(datum="K", left=None, right=None)
nodeL = TreeNode(datum="L", left=None, right=None)
nodeM = TreeNode(datum="M", left=None, right=None)
nodeD = TreeNode(datum="D", left=None, right=None)
nodeE = TreeNode(datum="E", left=nodeI, right=nodeJ)
nodeF = TreeNode(datum="F", left=nodeK, right=nodeL)
nodeH = TreeNode(datum="H", left=nodeM, right=None)
nodeB = TreeNode(datum="B", left=nodeD, right=nodeE)
nodeC = TreeNode(datum="C", left=nodeF, right=nodeH)
nodeA = TreeNode(datum="A", left=nodeB, right=nodeC)

# construct tree object
treeObj = MyBinaryTree()
treeObj.root = nodeA

# in-order print
print("In-order:")
treeObj.print_in_order()

# pre-order print
print("Pre-order:")
treeObj.print_pre_order()

# post-order print
print("Post-order:")
treeObj.print_post_order()