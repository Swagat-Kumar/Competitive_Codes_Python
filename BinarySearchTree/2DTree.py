class Node:
    def __init__(self, x=0, y=0, left=None, right=None) -> None:
        self.x = x
        self.y = y
        self.left = left
        self.right = right


def insert(root, x, y, level=0):
    if root == None:
        return Node(x, y)
    if level % 2 == 0:
        if x < root.x:
            root.left = insert(root.left, x, y, level+1)
        elif x >= root.x:
            root.right = insert(root.right, x, y, level+1)
        return root
    else:
        if y < root.y:
            root.left = insert(root.left, x, y, level+1)
        elif y >= root.y:
            root.right = insert(root.right, x, y, level+1)
        return root


root = None
root = insert(root, 3, 6)
root = insert(root, 2, 7)
root = insert(root, 17, 15)
root = insert(root, 6, 12)
root = insert(root, 13, 15)
root = insert(root, 9, 1)
root = insert(root, 10, 19)


def search(node, x, y, level=0):
    if node == None:
        return False
    if node.x == x and node.y == y:
        return True
    if level % 2 == 0:
        if x < node.x:
            return search(node.left, x, y, level+1)
        elif x > node.x:
            return search(node.right, x, y, level+1)
        else:
            return search(node.left, x, y, level+1) or search(node.right, x, y, level+1)
    else:
        if y < node.x:
            return search(node.left, x, y, level+1)
        elif y > node.y:
            return search(node.right, x, y, level+1)
        else:
            return search(node.left, x, y, level+1) or search(node.right, x, y, level+1)


print(search(root, 2, 77))
