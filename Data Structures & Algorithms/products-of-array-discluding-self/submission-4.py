class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        '''
        pre = 2
        1 2 4 6
        
        1 1 2 8
            16 8     
        
        post = 16

        '''
        prefix = 1
        for i in range(len(nums)):
            print(prefix)
            res[i] = prefix
            prefix *= nums[i]
        
        print(res)

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res