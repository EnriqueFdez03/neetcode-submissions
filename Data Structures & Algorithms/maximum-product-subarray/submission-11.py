class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = nums[0], nums[0]

        for num in nums[1:]:
            tmp = currMax
            currMax = max(currMin * num, currMax * num, num)
            currMin = min(currMin * num, tmp * num, num)
            res = max(currMax, res)
        
        return res