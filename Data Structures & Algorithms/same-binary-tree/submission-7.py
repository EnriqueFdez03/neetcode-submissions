# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs
        queue = deque([(p, q)])

        while queue:
            for _ in range(len(queue)):
                first, second = queue.popleft()
                if not first and not second:
                    continue
                if not first or not second or first.val != second.val:
                    return False
                
                queue.append((first.left, second.left))
                queue.append((first.right, second.right))

        return True
