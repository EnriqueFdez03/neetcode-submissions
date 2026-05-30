class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0] * len(height)
        post = [0] * len(height)

        maximum = 0
        for i, h in enumerate(height):
            maximum = max(maximum, height[i])
            pre[i] = maximum
        
        maximum = 0
        for i in range(len(height) - 1, -1, -1):
            maximum = max(maximum, height[i])
            post[i] = maximum
        
        res = 0
        for i in range(len(height)):
            res += min(pre[i], post[i]) - height[i]
        
        return res