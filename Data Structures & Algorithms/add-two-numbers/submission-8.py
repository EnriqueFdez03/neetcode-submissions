# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        node = dummy = ListNode()

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            
            if val > 9:
                carry = val // 10
                val = val % 10
            else:
                carry = 0
            node.next = ListNode(val)
            node = node.next
        
        if carry:
            node.next = ListNode(carry)
        
        return dummy.next