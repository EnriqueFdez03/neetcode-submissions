# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# divide and conquer solution
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, l, r):
        # divide and conquer approach using recursion
        # base case
        if l == r:
            return lists[l]
        if l > r:
            return None

        mid = l + (r - l) // 2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)
        return self.conquer(left, right)

    def conquer(self, l1: List[Optional[ListNode]], l2: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr, l1 = curr.next, l1.next
            else:
                curr.next = l2
                curr, l2 = curr.next, l2.next
        
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next
