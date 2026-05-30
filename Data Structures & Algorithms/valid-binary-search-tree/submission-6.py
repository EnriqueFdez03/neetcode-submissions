# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftMax = self.maxNode(root.left, None)
        rightMin = self.minNode(root.right, None)
        
        if leftMax and leftMax >= root.val:
            return False
        if rightMin and rightMin <= root.val:
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def minNode(self, root, currMin):
        if not root:
            return currMin
        if currMin == None or root.val < currMin:
            currMin = root.val
        
        return min(self.minNode(root.left, currMin), self.minNode(root.right, currMin)) 
        
    def maxNode(self, root, currMax):
        if not root:
            return currMax
        if currMax == None or root.val > currMax:
            currMax = root.val

        return max(self.maxNode(root.left, currMax), self.maxNode(root.right, currMax)) 