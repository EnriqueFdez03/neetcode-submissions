class Solution:
    def trap(self, height: List[int]) -> int:
        totalAmount = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right] 
        while left <= right:
            if maxLeft < maxRight:
                curr = maxLeft - height[left]
                totalAmount += curr if curr >= 0 else 0
                maxLeft = max(maxLeft, height[left])
                left += 1
            else:
                curr = maxRight - height[right]
                totalAmount += curr if curr >= 0 else 0
                maxRight = max(maxRight, height[right])
                right -= 1

        return totalAmount

    

