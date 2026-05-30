class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]

        for a, b in intervals:
            lastEnd = res[-1][1]

            if lastEnd >= a:
                res[-1][1] = max(b, lastEnd)
            else:
                res.append([a, b])
        return res