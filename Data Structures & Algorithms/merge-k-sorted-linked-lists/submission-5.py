# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while len(lists) > 1:
            lMin = lists[0]
            pos = 0
            for i, l in enumerate(lists):
                if l.val < lMin.val:
                    lMin = l
                    pos = i

            node.next = lMin
            node = node.next
            lMin = lMin.next
            if not lMin:
                lists.pop(pos)
            else:
                lists[pos] = lMin

        if len(lists) == 1:        
            node.next = lists[0]

        return dummy.next