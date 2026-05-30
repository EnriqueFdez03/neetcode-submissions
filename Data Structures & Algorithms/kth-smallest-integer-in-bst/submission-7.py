# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        res = root.val
        cnt = k
        def dfs(root):
            nonlocal cnt, res
            if not root:
                return

            dfs(root.left)
            if cnt == 0:
                return
            cnt -= 1
            if cnt == 0:
                res = root.val
                return res
            dfs(root.right)
        
        dfs(root)
        return res
