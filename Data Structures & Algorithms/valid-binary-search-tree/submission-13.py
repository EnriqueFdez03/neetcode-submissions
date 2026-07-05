# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node, leftMax, rightMin):
            if not node:
                return True
                
            return leftMax < node.val < rightMin and isValid(node.left, leftMax, node.val) and isValid(node.right, node.val, rightMin)
        
        return isValid(root, float('-inf'), float('inf'))