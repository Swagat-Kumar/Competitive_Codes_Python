"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.maxD = 0
        if root == None:
            return 0

        def visit(node, depth=1):
            if depth > self.maxD:
                self.maxD = depth
            for c in node.children:
                visit(c, depth+1)
        visit(root)
        return self.maxD
