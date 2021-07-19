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
    root = insert(root, int(line))


def ranger(root, lo, hi):
    if root == None:
        return
    if lo <= root.val:
        ranger(root.left, lo, hi)
    if root.val >= lo and root.val <= hi:
        print(root.val)
    if hi >= root.val:
        ranger(root.right, lo, hi)


for i in range(5):
    a, b = map(int, input().split())
    ranger(root, a, b)
