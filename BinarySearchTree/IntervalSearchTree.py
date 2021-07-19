class Node:
    def __init__(self, left=None, right=None, maxx=None) -> None:
        self.interval = [left, right]
        self.maxx = maxx
        self.left = None
        self.right = None


root = None


def maxer(node):
    if node == None:
        return 0
    return node.interval[1]


def insert(root, left, right):
    if root == None:
        return Node(left, right, right)
    if left < root.interval[0]:
        root.left = insert(root.left, left, right)
    elif left >= root.interval[0]:
        root.right = insert(root.right, left, right)
    root.maxx = max(maxer(root.left), maxer(root.right), right)
    return root


root = insert(root, 17, 19)
root = insert(root, 5, 8)
root = insert(root, 21, 24)
root = insert(root, 4, 8)
root = insert(root, 15, 18)
root = insert(root, 7, 10)
root = insert(root, 16, 22)


def solve(root, left, right):
    if root == None:
        return
    if root.interval[1] >= left and root.interval[0] <= right:
        print(root.interval)
    if root.left == None:
        solve(root.right, left, right)
    elif root.left.maxx < left:
        solve(root.right, left, right)
    else:
        solve(root.left, left, right)
        solve(root.right, left, right)


for i in range(5):
    a, b = map(int, input().split())
    solve(root, a, b)
