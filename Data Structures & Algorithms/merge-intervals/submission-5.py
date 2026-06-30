class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            a1, b1 = res[-1]
            a2, b2 = intervals[i]

            if a2 <= b1:
                res[-1][1] = max(b1, b2)
            else:
                res.append([a2, b2])

        return res