"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    '''
    this problem is equivalent to reply how many rooms are
    needed as maximum at a certain moment in time
    This is greedy. We can have time as array. We will
    add two tuples per interval. First item in tuple
    represents start time or end time, last item 1 or -1 (if end time)
    '''
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))

        time.sort(key=lambda x: (x[0], x[1])) # sort first based on time, then on -1 and 1

        count = 0
        res = 0
        for time, usage in time:
            count += usage
            res = max(res, count)

        return res
