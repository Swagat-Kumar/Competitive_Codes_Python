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
root = insert(root, 0)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 6)


def leftmost(node):
    if node.left == None:
        return node.val
    else:
        return leftmost(node.left)


def deleteMin(node):
    if node.left == None:
        return node.right
    node.left = deleteMin(node.left)
    return node


def Min(node):
    if node.left == None:
        return node
    else:
        return Min(node.left)


def delete(node, val):
    if node == None:
        return None
    if val < node.val:
        node.left = delete(node.left, val)
    elif val > node.val:
        node.right = delete(node.right, val)
    else:
        if node.right == None:
            return node.left
        if node.left == None:
            return node.right
        t = node
        node = Min(t.right)
        node.right = deleteMin(t.right)
        node.left = t.left
    return node


def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)


print("before")
inorder(root)
root = delete(root, 0)
print("after 0")
inorder(root)
root = delete(root, 1)
print("after 1")
inorder(root)
root = delete(root, 5)
print("after 5")
inorder(root)
