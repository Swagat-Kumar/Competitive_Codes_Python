"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        listA = []

        def visit(node):
            if node == None:
                return
            listA.append(node.val)
            for child in node.children:
                visit(child)
        visit(root)
        return listA
