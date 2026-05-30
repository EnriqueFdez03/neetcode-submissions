# if I remember properly this one can be solved in two passes, 
# left to right and reverse
# 0 2 2 3 3 3 3 3 3 3 postfix
# 3 3 3 3 3 3 3 3 2 1 prefix
# 0 0 2 0 2 3 2 0 0 0 = 9
# 0 2 0 3 1 0 1 3 2 1 input
class Solution:
    def trap(self, height: List[int]) -> int:
        postfix, prefix = [], []
        
        currMax = 0
        for h in height:
            currMax = max(currMax, h)
            postfix.append(currMax)
        
        currMax = 0
        for i in range(len(height)-1, -1, -1):
            currMax = max(currMax, height[i])
            prefix.insert(0, currMax)
        
        currSum = 0
        for i in range(len(height)):
            currSum += min(postfix[i], prefix[i]) - height[i]
        
        return currSum

