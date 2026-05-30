# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        if root == None:
            return False

        return self.equal(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def equal(self, q: Optional[TreeNode], p: Optional[TreeNode]) -> bool:
        if q is None or p is None:
            return q == p
        
        return q.val == p.val and self.equal(q.left, p.left) and self.equal(q.right, p.right)