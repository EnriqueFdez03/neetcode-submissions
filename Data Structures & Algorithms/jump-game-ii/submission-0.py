class Solution:
    def jump(self, nums: List[int]) -> int:
        # bfs but instead of using a queue, we use a window (l, r)
        res = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(nums[i] + i, farthest)
            
            l = r + 1
            r = farthest
            res += 1
        
        return res