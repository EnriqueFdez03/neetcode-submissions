# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 1 indexed
        # inorder traversal left -> node -> right
        cnt = 1
        res = None
        def dfs(node):
            nonlocal cnt, res
            if not node:
                return

            dfs(node.left)
            if cnt == k:
                res = node.val
            cnt += 1
            dfs(node.right)
            return res
        
        return dfs(root)