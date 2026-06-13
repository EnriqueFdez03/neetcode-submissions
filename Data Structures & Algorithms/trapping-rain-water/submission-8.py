class Solution:
    def trap(self, height: List[int]) -> int:
        post = []
        maxH = 0
        for h in height:
            maxH = max(maxH, h)
            post.append(maxH)
        
        pre = []
        maxH = 0
        for i in range(len(height) - 1, -1, -1):
            maxH = max(maxH, height[i])
            pre.append(maxH)
        pre.reverse()
        
        res = 0
        for i in range(len(height)):
            minH = min(post[i], pre[i])
            res += minH - height[i]
        
        return res