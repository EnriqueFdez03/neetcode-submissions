from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return [max(nums)]
        
        res = []
        queue = deque() # stores indexes, monotonically decreasing stack
        l = r = 0
        
        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop() 
            queue.append(r)

            # remove the left index after moving the window
            if l > queue[0]:
                queue.popleft()
            
            # if window has k size
            if r - l + 1 == k:
                res.append(nums[queue[0]])
                l += 1
            r += 1

        return res


  