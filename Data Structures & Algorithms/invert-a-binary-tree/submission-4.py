# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #trying bfs
        if not root:
            return
            
        queue = deque([root])

        while queue:
            node = queue.popleft() # same as [].pop(0), but it takes O(n) compared to O(1)
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root
