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

def Postorder(root):
    if root:
        Postorder(root.lc)
        Postorder(root.rc)
        print(root.nodedata)
Postorder(root)