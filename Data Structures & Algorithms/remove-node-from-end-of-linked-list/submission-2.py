# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0 or not head:
            return head
        
        self.printList(head)
        # reverse
        
        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        
        newHead, curr = prev, prev
        prev = None
        while curr:
            n -= 1
            if n == 0:
                if prev:
                    prev.next = curr.next
                else:
                    newHead = curr.next
                    break
            
            prev = curr
            curr = curr.next
        
        self.printList(newHead)

        # reverse again
        prev = None
        while newHead:
            nextNode = newHead.next
            newHead.next = prev
            prev = newHead
            newHead = nextNode
        
        return prev
    
    def printList(self, head):
        if not head:
            ""

        s = ""
        while head:
            s += str(head.val) + " -> "
            head = head.next
        s += " None"
        print(s)
        