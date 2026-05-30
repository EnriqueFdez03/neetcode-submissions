class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        # greedy idea. As we sorted via start, in case of overlapping
        # pick the interval with the lowest end time. 

        res = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            a0, a1 = intervals[i]

            if a0 < prevEnd:
                prevEnd = min(prevEnd, a1)
                res += 1
            else:
                prevEnd = a1 # this means no overlapping
        return res