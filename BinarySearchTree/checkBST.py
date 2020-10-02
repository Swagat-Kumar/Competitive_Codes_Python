def isBST(root):
    if root == None:
        return True
    # code here

    def check(node, maxi, mini):
        if node == None:
            return True
        if maxi != None:
            if node.data >= maxi:
                return False
        if mini != None:
            if node.data <= mini:
                return False
        left = check(node.left, node.data, mini)
        right = check(node.right, maxi, node.data)
        return left and right
    le = check(root.left, root.data, None)
    ri = check(root.right, None, root.data)
    return le and ri
