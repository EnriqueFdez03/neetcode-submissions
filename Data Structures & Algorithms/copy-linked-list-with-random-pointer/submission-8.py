"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCurr = { None: None }
        
        node = head
        while node:
            oldToCurr[node] = Node(node.val)
            node = node.next
        
        curr = head
        while curr:
            dummy = oldToCurr[curr]
            dummy.next = oldToCurr[curr.next]
            dummy.random = oldToCurr[curr.random]
            curr = curr.next
        return oldToCurr[head]