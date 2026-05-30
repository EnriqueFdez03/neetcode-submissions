# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs -> deque + popleft
        if not root:
            return []

        nodes = deque([root])

        acum = []
        while nodes:
            level = []
            for _ in range(len(nodes)):
                cur = nodes.popleft()
                level.append(cur.val)
                if cur.left:
                    nodes.append(cur.left)
                if cur.right:
                    nodes.append(cur.right)
            acum.append(level)
        
        return acum
        
