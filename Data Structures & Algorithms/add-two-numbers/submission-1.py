# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy
        carry = 0
        while l1 and l2:
            acum = l1.val + l2.val + carry
            if acum >= 10:
                carry = 1
                acum -= 10
            else:
                carry = 0
            res.next = ListNode(acum)
            l1, l2, res = l1.next, l2.next, res.next
        
        while l1:
            acum = l1.val + carry
            if acum >= 10:
                carry = 1
                acum -= 10
            else:
                carry = 0
            res.next = ListNode(acum)
            l1, res = l1.next, res.next

        while l2:
            acum = l2.val + carry
            if acum >= 10:
                carry = 1
                acum -= 10
            else:
                carry = 0
            res.next = ListNode(acum)
            l2, res = l2.next, res.next
        
        if carry == 1:
            res.next = ListNode(carry)
        
        self.printList(dummy.next)

        return dummy.next

    def printList(self, head):
        s = ""
        while head:
            s += str(head.val) + " -> "
            head = head.next
        s += "None"
        print(s)
