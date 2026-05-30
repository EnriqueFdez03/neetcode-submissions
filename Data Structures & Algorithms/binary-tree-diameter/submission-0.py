# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # apply dfs: remember the height problem
        res = 0 # to be modified inside the nested dfs function

        def dfs(root): # we will calculate the height left and right. Everytime, store in res the biggest diameter
            nonlocal res # nonlocal allows us to modify the outer var res inside a nested function
            if not root: return 0

            leftH = dfs(root.left) 
            rightH = dfs(root.right)

            # modify res
            res = max(res, leftH + rightH)

            return 1 + max(leftH, rightH) # height at node x.
        
        dfs(root)
        return res

