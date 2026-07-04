class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy solution, as we sorted based on start pick the one with smallest end
        if len(intervals) < 2:
            return 0
        intervals.sort(key=lambda x: x[0])
        
        res = 0
        smallestEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if smallestEnd > a:
                res += 1
                smallestEnd = min(b, smallestEnd)
            else:
                smallestEnd = b

        return res
