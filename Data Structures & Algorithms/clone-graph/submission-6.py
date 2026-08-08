"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = { None: None }

        def dfs(node):
            nonlocal oldToNew 
            
            if node in oldToNew:
                return oldToNew[node]
            
            oldToNew[node] = Node(node.val)
            oldToNew[node].neighbors = [dfs(nei) for nei in node.neighbors]
            return oldToNew[node]
        
        return dfs(node)