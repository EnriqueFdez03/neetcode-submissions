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
            nextLevel = []
            curLevel = []
            for _ in range(len(nodes)):
                cur = nodes.popleft()
                curLevel.append(cur.val)
                if cur.left:
                    nextLevel.append(cur.left)
                if cur.right:
                    nextLevel.append(cur.right)
            acum.append(curLevel)
            nodes.extend(nextLevel)
        
        return acum
        
