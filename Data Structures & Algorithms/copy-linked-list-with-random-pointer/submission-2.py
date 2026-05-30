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
        hashMap = {None: None}

        curr = head
        while curr:
            node = Node(curr.val)
            hashMap[curr] = node
            curr = curr.next

        curr = head
        while curr:
            currNode = hashMap[curr]
            currNode.next = hashMap[curr.next]
            currNode.random = hashMap[curr.random]
            curr = curr.next

        return hashMap[head]