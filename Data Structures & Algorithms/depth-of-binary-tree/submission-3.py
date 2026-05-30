# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxD = 0

        stack = [(root, 1)]
        while stack:
            node, currD = stack.pop()
            maxD = max(maxD, currD)
            if node.left:
                stack.append((node.left, currD + 1))
            if node.right:
                stack.append((node.right, currD + 1))
        
        return maxD