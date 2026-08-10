class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
            ......                  .........           ................
                    ......              ..........          .......
        '''
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            a, b = res[-1]
            c, d = intervals[i]

            if b < c:
                res.append([c, d])
                continue
            if c <= b:
                res[-1][0] = min(a, c)
                res[-1][1] = max(b, d)

        return res