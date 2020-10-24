"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        listA = []
        if root == None:
            return None

        def visit(node):
            for c in node.children:
                visit(c)
            listA.append(node.val)
        visit(root)
        return listA
