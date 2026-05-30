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
        if not head:
            return None
        # hashmap is the key
        oldToCopy = dict()
        
        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        dummy = None
        while curr:
            dummy = oldToCopy[curr]
            if curr.next:
                dummy.next = oldToCopy[curr.next]
            if curr.random:
                dummy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]