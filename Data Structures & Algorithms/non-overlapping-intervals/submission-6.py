class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        cache = {}
        n = len(intervals)
        def dfs(i, lastKeptEnd): # i to pick or not to pick depending on i + 1
            if i >= n:
                return 0
            if (i, lastKeptEnd) in cache:
                return cache[(i, lastKeptEnd)]
            if lastKeptEnd == None:  
                return dfs(i + 1, intervals[i][1])

            a0, a1 = intervals[i]
            if a0 < lastKeptEnd:
                res = min(1 + dfs(i + 1, a1), 1 + dfs(i + 1, lastKeptEnd))
                cache[(i, lastKeptEnd)] = res
                return res
            res = dfs(i + 1, a1)
            cache[(i, lastKeptEnd)] = res
            return res
        return dfs(0, None)