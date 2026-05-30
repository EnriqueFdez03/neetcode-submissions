# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # REMEMBER BST NODES ARE SORTED, WHICH MEANS, left < parent < right FOR ALL Nodes including, nietos

        if not root:
            return
        
        maxV = max(p.val, q.val)
        minV = min(p.val, q.val)
        if minV <= root.val <= maxV:
            return root
        elif max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)       