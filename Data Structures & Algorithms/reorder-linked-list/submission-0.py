# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        prev = None
        # reverse second 4 -> 5 -> 6 -> None
        while second:
            nextNode = second.next # 5 -> ... / 6 -> None / None
            second.next = prev  # 4 -> None / 5 -> 4 -> None / 6 -> 5 -> 4 -> None
            prev = second # prev = 5 / 5 -> 4 -> None / 6 -> 5 -> 4 -> None
            second = nextNode # 5 -> ...  / 6 -> None / None
   
        second = prev
        first = head
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2