# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #use bfs
        res = []
        queue = deque([root])
        while queue:
            rightMost = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                rightMost = node.val

                queue.append(node.left)
                queue.append(node.right)
            if rightMost:
                res.append(rightMost)
        return res