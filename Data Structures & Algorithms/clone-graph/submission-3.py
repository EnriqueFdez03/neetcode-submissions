"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(root):
            if not root:
                return
            if root not in oldToNew:
                copy = Node(root.val)
                oldToNew[root] = copy
            copy = oldToNew[root]

            for nei in root.neighbors:
                if nei in oldToNew:
                    copyNei = oldToNew[nei]
                else:
                    copyNei = dfs(nei)
                copy.neighbors.append(copyNei)
            return copy

        return dfs(node) if node else None