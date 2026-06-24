# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderDict = { n:i for i, n in enumerate(inorder)}
        
        preIdx = 0
        def dfs(l, r):
            nonlocal preIdx
            
            if l > r:
                return

            node = TreeNode(preorder[preIdx])
            midPoint = inOrderDict[preorder[preIdx]]
            preIdx += 1

            node.left = dfs(l, midPoint - 1) 
            node.right = dfs(midPoint + 1, r)

            return node
        
        return dfs(0, len(preorder) - 1)