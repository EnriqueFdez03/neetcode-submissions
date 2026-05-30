# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head

        totalLength = 0
        while first:
            totalLength += 1
            first = first.next

        # 0 based index
        index = totalLength - n
        if index == 0:
            return head.next
        
        curr = head
        while index - 1 != 0:
            curr = curr.next
            index -= 1
        
        curr.next = curr.next.next
        return head
