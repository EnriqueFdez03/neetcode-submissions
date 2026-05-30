class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        maxLen = 0
        for i in range(len(nums)):
            cand = nums[i]
            currLen = 1
            while (cand + 1) in numsSet:
                currLen += 1
                cand = cand + 1
            
            maxLen = currLen if currLen > maxLen else maxLen
        
        return maxLen