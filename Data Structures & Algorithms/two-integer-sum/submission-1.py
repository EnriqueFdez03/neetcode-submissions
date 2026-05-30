class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = 1

        while True:
            a = nums[low]
            b = nums[high]

            if a + b == target:
                return [low, high]
            else:
                if high != len(nums) - 1:
                    high += 1
                else: 
                    low += 1
                    high = low + 1

                    if high == len(nums):
                        break 
