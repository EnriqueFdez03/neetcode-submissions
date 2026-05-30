# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        copy = head
        while head and copy:
            head = head.next
            copy = copy.next
            if copy:
                copy = copy.next
            else:
                return False
            if head == copy:
                return True
            
        return False