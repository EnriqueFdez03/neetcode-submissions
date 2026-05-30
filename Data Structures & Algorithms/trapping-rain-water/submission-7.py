class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if height[l] < height[r]:
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]
                l += 1
            else:
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]
                r -= 1

        return res