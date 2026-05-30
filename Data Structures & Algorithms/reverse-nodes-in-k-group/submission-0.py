# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, end):
        prev, curr = None, head
        while curr != end:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # using a recursive approach
        # obtain the node kth (starting index = 0)
        nextGroup = head # 3 -> 4
        count = 0
        while nextGroup and count < k:
            nextGroup = nextGroup.next
            count += 1
        if count < k:
            return head # base case

        newHead = self.reverse(head, nextGroup) # 2 -> 1
        head.next = self.reverseKGroup(nextGroup, k) # (2 ..> ) 1 -> NRecursiveCall (4 -> 3)
        return newHead
