# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative dfs: stack + pop() 
        if not root:
            return 0

        stack = [(root, 1)]
        maxLevel = 1
        while stack:
            node, level = stack.pop()
            maxLevel = max(maxLevel, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
            
        return maxLevel
        