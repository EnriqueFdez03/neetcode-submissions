# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle point
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # unlink the first half to the second one
        middle = slow.next
        slow.next = None

        prev = None
        while middle:
            nextNode = middle.next
            middle.next = prev
            prev = middle
            middle = nextNode
        
        secondHalf = prev
        dummy = node = ListNode()
        while secondHalf:
            next1 = head.next
            next2 = secondHalf.next

            node.next = head
            node = node.next
            node.next = secondHalf
            node = node.next
            
            head = next1
            secondHalf = next2
        if head: 
            node.next = head

        head = dummy.next
