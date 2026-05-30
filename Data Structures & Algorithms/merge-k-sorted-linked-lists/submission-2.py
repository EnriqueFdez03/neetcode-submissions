import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()

        minHeap = []
        for l in lists:
            if l:
                heapq.heappush(minHeap, NodeWrapper(l))
            
        while minHeap:
            minNode = heapq.heappop(minHeap).node
            curr.next = minNode
            curr = curr.next

            if minNode.next:
                heapq.heappush(minHeap, NodeWrapper(minNode.next))

        return dummy.next