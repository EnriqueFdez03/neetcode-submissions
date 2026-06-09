# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()
        total, completed = sum(l != None for l in lists), 0

        while completed < total:
            smallest, idx = float('inf'), -1
            for i in range(len(lists)):
                if lists[i] and smallest > lists[i].val:
                    smallest = lists[i].val
                    idx = i

            l = lists[idx]
            node.next = l
            node = node.next
            lists[idx] = l.next
            if not l.next:
                completed += 1
        
        return dummy.next