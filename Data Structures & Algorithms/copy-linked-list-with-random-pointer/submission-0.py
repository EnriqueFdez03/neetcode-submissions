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
        hashMap = {}

        curr = head
        first = None
        while curr:
            node = Node(curr.val)
            if not first:
                first = node
            hashMap[curr] = node
            curr = curr.next

        while head:
            currNode = hashMap[head]
            currNode.next = hashMap[head.next] if head.next else None
            currNode.random = hashMap[head.random] if head.random else None
            head = head.next

        return first