import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negs = [-n for n in nums]
        heapq.heapify(negs)

        res = None
        while k > 0:
            k -= 1
            res = -heapq.heappop(negs)
        
        return res