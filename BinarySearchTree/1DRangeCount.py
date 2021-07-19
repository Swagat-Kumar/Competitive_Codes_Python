class Node:
    def __init__(self, val=0, left=None, right=None, rank=0, count=0):
        self.val = val
        self.left = left
        self.right = right
        self.count = count
        self.rank = rank


def size(node):
    if node == None:
        return 0
    else:
        return node.count


def insert(root, val):
    if root == None:
        return Node(val, None, None, 0, 1)
    if root.val == val:
        return root
    elif val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    root.count = 1+size(root.left)+size(root.right)
    return root


root = None
while True:
    line = input()
    if line == "exit.":
        break
    root = insert(root, int(line))


def inorder(node, val):
    if node == None:
        return 0
    if val < node.val:
        return inorder(node.left, val)
    elif val > node.val:
        return 1+size(node.left)+inorder(node.right, val)
    else:
        return size(node.left)


print(inorder(root, 75))
