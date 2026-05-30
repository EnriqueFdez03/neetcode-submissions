# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()

        while any(lists):
            smallest, idx = lists[0], 0
            for i, l in enumerate(lists):  
                if not smallest or (l and l.val < smallest.val):
                    smallest, idx = l, i
            
            curr.next = smallest
            curr, smallest = curr.next, smallest.next
            lists[idx] = smallest

        return dummy.next
