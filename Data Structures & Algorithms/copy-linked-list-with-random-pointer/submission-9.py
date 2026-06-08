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
        currToCopy = { None: None }

        node = head
        while node:
            currToCopy[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            currToCopy[node].next = currToCopy[node.next]
            currToCopy[node].random = currToCopy[node.random]
            node = node.next

        return currToCopy[head]