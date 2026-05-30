class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def aux(houses):
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(dp[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            
            return dp[-1]
        
        return max(aux(nums[:-1]), aux(nums[1:]))