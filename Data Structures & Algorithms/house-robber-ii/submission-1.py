class Solution:
    def rob(self, nums: List[int]) -> int:
        # WHY this is wrong, the reason is that firstRobbed has to form
        # part of the state as well. IT is not the same dfs(1, True) dfs(1, False)
        cache = {}
        def dfs(i, firstRobbed):
            if i >= len(nums):
                return 0
            if (i, firstRobbed) in cache:
                return cache[(i, firstRobbed)]
            if i == len(nums) - 1 and firstRobbed:
                return 0
            
            firstOpt = nums[i] + dfs(i + 2, i == 0 or firstRobbed)
            secondOpt = dfs(i + 1, firstRobbed)

            cache[(i, firstRobbed)] = max(firstOpt, secondOpt)
            return cache[(i, firstRobbed)]

        return dfs(0, False)
        '''
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = max(nums[0], nums[-1])
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[-1]
        '''