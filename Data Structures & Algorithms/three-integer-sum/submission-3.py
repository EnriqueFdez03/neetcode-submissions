class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low, high = i + 1, len(nums) - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]

                if s == 0:
                    triplets.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1

                    while low < len(nums) - 1 and nums[low] == nums[low - 1]:
                        low += 1
                    while high > i and nums[high] == nums[high + 1]:
                        high -= 1
                elif s > 0:
                    high -= 1
                else:
                    low += 1                  
        return triplets