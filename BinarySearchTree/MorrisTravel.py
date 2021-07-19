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
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 5)
root = insert(root, 8)
root = insert(root, 9)
root = insert(root, 10)
root = insert(root, 0)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)


current = root
while current != None:
    if current.left == None:
        print(current.val)
        current = current.right
    else:
        pred = current.left
        while pred.right != current and pred.right != None:
            pred = pred.right
        if pred.right == None:
            pred.right = current
            current = current.left
        else:
            pred.right = None
            print(current.val)
            current = current.right
