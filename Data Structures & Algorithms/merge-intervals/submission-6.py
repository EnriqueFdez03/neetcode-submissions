class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            a, b = res[-1]
            c, d = intervals[i]

            if b < c:
                res.append([c, d])
            else:
                res[-1][0] = min(intervals[i][0], res[-1][0])
                res[-1][1] = max(intervals[i][1], res[-1][1])

        return res