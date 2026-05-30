class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                pivot = num

                if pivot + nums[left] + nums[right] < 0:
                    left += 1
                elif pivot + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([pivot, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1
                    while nums[right + 1] == nums[right] and left < right:
                        right -= 1
        
        return res
