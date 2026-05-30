# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterative
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        stack = [(p, q)]
        while stack:
            first, second = stack.pop()
            if not first and not second:
                continue
            if (not first or not second) or first.val != second.val:
                return False
            stack.append((first.left, second.left))
            stack.append((first.right, second.right))

        return True
