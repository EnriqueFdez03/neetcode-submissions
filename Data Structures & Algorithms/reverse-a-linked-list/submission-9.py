# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # never it is too late to repeat this exercise!
        # -> 0 -> 1 -> 2 -> 3 ->
        # <- 0 <- 1 <- 2 <- 3 <- 
        prev = None
        while head:
            nextHead = head.next
            head.next = prev
            prev = head
            head = nextHead
        return prev