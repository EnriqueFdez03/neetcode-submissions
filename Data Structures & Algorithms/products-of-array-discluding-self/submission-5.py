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
        preMult = [1] * len(nums)
        for i, num in enumerate(nums):
            preMult[i] *= pre
            pre *= num
        
        post = 1
        postMult = [1] * len(nums)
        for i, num in enumerate(reversed(nums)):
            postMult[len(nums) - 1 - i] *= post
            post *= num
        
        res = []
        for preNum, postNum in zip(preMult, postMult):
            res.append(preNum * postNum)

        return res