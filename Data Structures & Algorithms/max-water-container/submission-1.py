class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        low, high = 0, len(heights) - 1
        while low < high:
            leftH, highH = heights[low], heights[high]
            currMax = max(currMax, (high - low) * min(leftH, highH))
            if leftH > highH:
                high -= 1
            else:
                low += 1
        
        return currMax