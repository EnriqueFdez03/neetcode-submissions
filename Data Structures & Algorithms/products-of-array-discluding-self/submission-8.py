class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1      2      4      6 questions: can we have empty values, do they count as 0?can we have values such as float(inf)? if the input list is empty, do you want as a result an empty list or [0]?
        
        #   1      2        4      6
        # 2*4*6  1*4*6    1*2*6   1*2*4
        #   1*     1*1     1*2    1*2*4  
        #  2*4*6  1*4*6    1*6      1

        res = [] 
        pre = 1
        for num in nums:
            res.append(pre)
            pre *= num
        
        post = 1
        for i, num in enumerate(nums[::-1]):
            res[len(nums) - i - 1] *= post
            post *= num
        
        return res

