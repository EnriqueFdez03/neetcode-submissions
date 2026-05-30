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
        while l1 or l2 or carry > 0:
            acum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if acum >= 10:
                carry = 1
                acum -= 10
            else:
                carry = 0
            res.next = ListNode(acum)
            l1, l2, res = l1.next if l1 else None, l2.next if l2 else None, res.next
        
        self.printList(dummy.next)
        return dummy.next

    def printList(self, head):
        s = ""
        while head:
            s += str(head.val) + " -> "
            head = head.next
        s += "None"
        print(s)
