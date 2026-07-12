class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1        2          4           6
        48       24         12          8

        2*4*6   1*4*6     1*2*6        1*2*4


PRE      1        1        1*2         1 *2*4    
POST    2*4*6    4*6        6            1     



        '''
        pre = 1
        res = [1] * len(nums)
        for i, num in enumerate(nums):
            res[i] *= pre
            pre *= num
        
        post = 1
        for i, num in enumerate(reversed(nums)):
            res[len(nums) - 1 - i] *= post
            post *= num

        return res