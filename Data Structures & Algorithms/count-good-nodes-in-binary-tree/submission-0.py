# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, currMax):
            nonlocal res
            if not node:
                return
            
            if not currMax or node.val >= currMax:
                res += 1
                currMax = node.val

            if node.left:
                dfs(node.left, currMax)
            if node.right:
                dfs(node.right, currMax)

        dfs(root, None)
        return res