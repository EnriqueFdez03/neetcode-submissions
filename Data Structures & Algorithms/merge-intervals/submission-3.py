class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            a1, b1 = res[-1]
            a2, b2 = intervals[i]
            if b1 >= a2:
                res[-1][1] = max(b1, b2)
            else:
                res.append([a2, b2])
        return res
