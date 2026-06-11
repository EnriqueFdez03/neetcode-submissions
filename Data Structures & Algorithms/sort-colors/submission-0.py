class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        counter = [0] * 3

        for num in nums:
            counter[num] += 1
        
        for i in range(n):
            j = 0
            while counter[j] == 0:
                j += 1
            nums[i] = j
            counter[j] -= 1