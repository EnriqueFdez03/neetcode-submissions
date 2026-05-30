# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()

        while True:
            minIdx = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue

                node = lists[i]
                if minIdx == -1 or lists[i].val < lists[minIdx].val:
                    minIdx = i
            
            if minIdx == -1:
                break

            curr.next = lists[minIdx]
            curr = curr.next
            lists[minIdx] = lists[minIdx].next

        return dummy.next
