class Solution:
    def trap(self, height: List[int]) -> int:
        maxAltitude = 0
        ltor = [0] * len(height)
        for i in range(len(height)):
            maxAltitude = max(height[i], maxAltitude)
            ltor[i] = maxAltitude
        
        maxAltitude = 0
        rtol = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            maxAltitude = max(height[i], maxAltitude)
            rtol[i] = maxAltitude

        totalAmount = 0
        for i in range(len(height)):
            curr = min(ltor[i], rtol[i]) - height[i]
            totalAmount += curr

        return totalAmount

