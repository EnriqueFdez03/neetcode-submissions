class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1st- sort intervals based on a0
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        
        for a0, a1 in intervals:
            lastEnd = res[-1][1]

            if lastEnd >= a0:
                res[-1][1] = max(lastEnd, a1)
            else:
                res.append([a0, a1])
        
        return res