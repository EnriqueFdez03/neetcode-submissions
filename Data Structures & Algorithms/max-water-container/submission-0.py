class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def areaCalculation(idxA, idxB):
            minHeight = min(heights[idxA], heights[idxB])
            distance = idxB - idxA
            
            return minHeight * distance
        
        
        left = 0
        right = len(heights) - 1
        maxWater = 0
        while left < right:
            maxWater = max(maxWater, areaCalculation(left, right))
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxWater


        