class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root, val):
    if root == None:
        return Node(val)
    if root.val == val:
        return root
    elif val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


root = None
while True:
    line = input()
    if line == "exit.":
        break
    root = insert(root, line)


def preorder(node):
    if node == None:
        print("None")
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node == None:
        print("None")
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


preorder(root)
print("Inorder")
inorder(root)
