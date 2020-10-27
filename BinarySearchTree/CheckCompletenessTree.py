# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        def complete(root):
            if root == None:
                return True
            queue = [root]
            flag = False
            while len(queue) != 0:
                node = queue.pop(0)
                if node.left:
                    if flag:
                        return False
                    queue.append(node.left)
                else:
                    flag = True
                if node.right:
                    if flag:
                        return False
                    queue.append(node.right)
                else:
                    flag = True
            return True
        return complete(root)
