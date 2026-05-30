class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longestSeq = 0
        for num in nums:
            currSol = 0
            if num - 1 not in numSet:
                currNum = num
                while currNum in numSet:                
                    currSol += 1
                    currNum += 1

                longestSeq = max(currSol, longestSeq)     

        return longestSeq