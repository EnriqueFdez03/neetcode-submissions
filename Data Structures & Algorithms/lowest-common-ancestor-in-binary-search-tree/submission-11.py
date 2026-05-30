# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        it is a bst so left values are smaller than root val and right values larger
        if:
            p val <= root.val <= q val -> res: root
            p val, q val <= root.val -> recursive case with root.left
            else: recursive case with root.right
        '''
        val1 = min(p.val, q.val)
        val2 = max(p.val, q.val)
        if val1 <= root.val and root.val <= val2:
            return root
        elif val1 <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)