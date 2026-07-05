# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pVal = min(p.val, q.val)
        qVal = max(p.val, q.val)
        
        if pVal <= root.val <= qVal:
            return root
        if qVal < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if pVal > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        