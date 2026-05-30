class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longestSeq = 0
        currSol = 0
        for num in nums:
            if num - 1 in numSet:
                continue

            currNum = num
            while currNum in numSet:                
                currSol += 1
                currNum += 1

            if currSol > longestSeq:
                longestSeq = currSol     
            currSol = 0

        return longestSeq