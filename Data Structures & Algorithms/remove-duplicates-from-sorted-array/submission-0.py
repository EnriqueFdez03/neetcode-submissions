class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        l, r = 0, 0
        while r < len(nums):
            while r + 1 < len(nums) and nums[r + 1] == nums[r]:
                r += 1
            
            nums[l] = nums[r]
            l += 1
            r += 1
        return l
