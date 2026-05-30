from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0
        for num in numSet:
            if not num - 1 in numSet:
                length = 1
                while num + length in numSet:
                    length += 1
                maxLength = max(maxLength, length)

        return maxLength