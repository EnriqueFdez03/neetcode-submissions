# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0 or not head:
            return head
        
        dummy = ListNode(0, head)
        left, right = dummy, head
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        
        return dummy.next
    
    def printList(self, head):
        if not head:
            ""

        s = ""
        while head:
            s += str(head.val) + " -> "
            head = head.next
        s += " None"
        print(s)
        