"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        intervals.sort(key=lambda x:x.start)
        
        heap = []
        roomsReq = 1
        
        heapq.heappush(heap, intervals[0].end)
        for i in range(1, len(intervals)):
            a, b = intervals[i].start, intervals[i].end
            b1 = heap[0]
            if b1 > a:
                heapq.heappush(heap, intervals[i].end)
                roomsReq = max(roomsReq, len(heap))
            else:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i].end)

        return roomsReq