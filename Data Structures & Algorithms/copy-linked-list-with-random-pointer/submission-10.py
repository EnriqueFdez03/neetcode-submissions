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
        # space optimized
        # A -> A´ -> B -> B' -> C -> C'
        # but how we connect random with their pointers?
        # let:
        # A.random = C
        # A.next = A'
        # We want A'.random = C'
        # so: A'.random = A.random(C).next

        if head is None:
            return None
        
        # A -> A' -> B -> B' ...
        node = head
        while node:
            copy = Node(node.val)
            copy.next = node.next
            node.next = copy
            node = copy.next
        
        newHead = head.next

        # Add randoms
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        
        # interleaving
        l1 = head
        while l1:
            l2 = l1.next
            l1.next = l2.next
            if l2.next:
                l2.next = l2.next.next
            l1 = l1.next
        
        return newHead