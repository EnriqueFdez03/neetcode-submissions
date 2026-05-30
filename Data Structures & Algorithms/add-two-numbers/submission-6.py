# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = node = ListNode()
        while l1 or l2:
            sumVal = carry
            if l1:
                sumVal += l1.val
                l1 = l1.next
            if l2:
                sumVal += l2.val
                l2 = l2.next

            if sumVal > 9:
                carry = sumVal // 10
                sumVal = sumVal % 10
            else:
                carry = 0
            node.next = ListNode(sumVal)
            node = node.next
            
        
        if carry > 0:
            node.next = ListNode(carry)
        
        return dummy.next
        
