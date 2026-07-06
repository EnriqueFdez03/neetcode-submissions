class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = nums[0], nums[0]

        for num in nums[1:]:
            temp = currMax
            currMax = max(num, currMax * num, currMin * num)
            currMin = min(num, currMin * num, temp * num)
            res = max(res, currMax)
        
        return res