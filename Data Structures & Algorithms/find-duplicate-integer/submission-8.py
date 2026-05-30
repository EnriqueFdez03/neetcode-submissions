class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        def realN(num):
            if num > size:
                return num % size
            else:
                return num
        def realIns(num):
            if num > size:
                return num // size
            else:
                return num

        for i, n in enumerate(nums): # 1 - 2- 3- 4 
            print(nums)
            n = realN(n)
            corr = nums[n - 1]
            if i != n - 1 and realIns(corr) == n:
                return n
            
            nums[n - 1] += n * size


                
            
