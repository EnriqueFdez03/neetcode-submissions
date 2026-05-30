class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (idx, h)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                (pos, height) = stack.pop()
                maxArea = max(maxArea, (i - pos) * height)
                start = pos
            stack.append((start, h))

        print(stack)
        for (i, h) in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        
        return maxArea


