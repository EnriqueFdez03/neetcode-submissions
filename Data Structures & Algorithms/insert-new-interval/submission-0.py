class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        res = []
        #
        #  ....     ........   .....
        #     ....    ....            .....
        # Check no collision and add the ones it does not collide
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # [a, b] [c, d] -> collision if max(a, c) <= min(b, d)
        while i < n and (max(intervals[i][0], newInterval[0]) <= min(intervals[i][1], newInterval[1])):
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)

        # add the remaining ones
        while i < n:
            res.append(intervals[i])
            i += 1

        return res