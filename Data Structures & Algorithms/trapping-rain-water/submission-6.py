class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        post, pre = [0] * n, [0] * n

        postMax = height[0]
        for i in range(n):
            post[i] = max(postMax - height[i], 0)
            postMax = max(postMax, height[i])

        preMax = height[-1]
        for i in range(n - 1, -1, -1):
            pre[i] = max(preMax - height[i], 0)
            preMax = max(preMax, height[i])

        res = 0
        for i in range(n):
            res += min(post[i], pre[i])

        return res