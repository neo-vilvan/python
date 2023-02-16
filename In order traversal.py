#Tree Traversal
#creating the tree

class Node:
    def __init__(self, val):
        self.lc = None
        self.rc = None
        self.nodedata = val

root = Node(1)
root.lc = Node(2)
root.rc = Node(3)
root.lc.lc = Node(4)
root.lc.rc = Node(5)

#In-order
def Inorder(root):
    if root:
        Inorder(root.lc)
        print(root.nodedata)
        Inorder(root.rc)
Inorder(root)