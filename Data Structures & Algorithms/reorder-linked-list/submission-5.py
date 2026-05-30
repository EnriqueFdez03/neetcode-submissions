# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find middle point
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        slow.next = None
        
        # reverse
        # 0 -> 1 -> 2 ->
        # <- 0 <- 1 <- 2
        prev = None
        while middle:
            nextHead = middle.next
            middle.next = prev
            prev = middle
            middle = nextHead
        secondHalf = prev

        # join both
        sol = dummy = ListNode()
        while head and secondHalf:
            tmp1 = head.next
            tmp2 = secondHalf.next

            dummy.next = head
            dummy = dummy.next
            dummy.next = secondHalf
            dummy = dummy.next 

            head = tmp1
            secondHalf = tmp2
        dummy.next = head or secondHalf
        
        head = sol.next
