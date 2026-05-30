# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative bfs: dequeue + popleft() 
        queue = deque()
        if root:
            queue.append(root)

        level = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        
        return level
        
        '''

        queue = [(root, 1)]
        maxLevel = 1
        while stack:
            node, level = stack.pop()
            maxLevel = max(maxLevel, level)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
            
        return maxLevel
        '''