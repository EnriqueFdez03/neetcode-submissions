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

        def dfs(node):
            if not node:
                return
            if node not in oldToNew:
                oldToNew[node] = Node(node.val)
            
            new = oldToNew[node]
            new.neighbors = [oldToNew[nei] if nei in oldToNew else dfs(nei) for nei in node.neighbors]

            return new

        return dfs(node)
