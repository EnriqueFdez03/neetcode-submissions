from heapq import heappop, heappush, heapify
from collections import defaultdict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return [max(nums)]
        
        res = []
        heap = []
        for i in range(len(nums)):            
            heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heappop(heap)
                res.append(-heap[0][0])
        
        return res


