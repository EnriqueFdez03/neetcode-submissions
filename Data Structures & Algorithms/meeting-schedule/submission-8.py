"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True

        intervals.sort(key= lambda x: x.start)
        
        b1 = intervals[0].end
        for i in range(1, len(intervals)):
            curr = intervals[i]
            a2, b2 = curr.start, curr.end
            if b1 > a2:
                return False
            b1 = b2
        
        return True