# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # post order dfs?
        parent = root.val
        res = 0
        def dfs(root, maxVal):
            nonlocal res
            if not root:
                return 0
            
            maxVal = max(maxVal, root.val)
            if root.val >= maxVal:
                res += 1

            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root, parent)

        return res