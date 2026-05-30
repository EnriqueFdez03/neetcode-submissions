class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                temp2, idx2 = stack.pop()
                res[idx2] = idx - idx2
            stack.append((temp, idx))
        
        return res