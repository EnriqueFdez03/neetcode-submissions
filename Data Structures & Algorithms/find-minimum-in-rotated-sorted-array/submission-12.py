class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        
        l, r = 0, len(nums) - 1
        while True:
            if r - l == 1:
                return min(nums[l], nums[r])

            m = (r + l) // 2
            if nums[l] < nums[m]:
                if nums[m] > nums[r]:
                    l = m
                else:
                    r = m
            else:
                r = m
            
            print(l, r)


         