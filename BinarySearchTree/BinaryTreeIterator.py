# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.listA = []

        def visit(node):
            if node == None:
                return
            visit(node.left)
            self.listA.append(node.val)
            visit(node.right)
        visit(root)
        self.current = 0

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.current += 1
        return self.listA[self.current-1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.current < len(self.listA)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
