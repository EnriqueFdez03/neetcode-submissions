# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        slow.next = None

        # reverse secondHalf
        prev = None
        while secondHalf:
            nextNode = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = nextNode
        
        # intercalate
        dummy = newHead = ListNode()
        l1, l2 = head, prev
        while l1 and l2:
            nextL1, nextL2 = l1.next, l2.next
            # 1 -> 2 -> 3 
            # 6 -> 5 -> 4
            newHead.next = l1
            newHead = newHead.next
            newHead.next = l2
            newHead = newHead.next
            l1 = nextL1
            l2 = nextL2
        
        newHead.next = l1 or l2
        
        head = dummy.next



