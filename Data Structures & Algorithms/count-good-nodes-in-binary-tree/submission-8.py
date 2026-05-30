# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, currMax):
            if not node:
                return 0
            
            res = 0
            if node.val >= root.val and node.val >= currMax:
                res += 1
            
            currMax = max(currMax, node.val)
            return res + dfs(node.left, currMax) + dfs(node.right, currMax)
        
        return dfs(root, root.val)