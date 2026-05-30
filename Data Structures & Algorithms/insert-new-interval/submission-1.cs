public class Solution {
    public int[][] Insert(int[][] intervals, int[] newInterval) {
        List<int[]> res = new List<int[]>();

        int i = 0;
        int n = intervals.Count();
        /*
            ....       .....       ......  [a, b]  a <= d && c <= b
                  ....    ....       ...   [c, d]
        */ 
        while (i < n && intervals[i][1] < newInterval[0]) {
            res.Add(intervals[i]);
            i += 1;
        }
        // b only gets bigger every time given that the intervals are sorted
        // and c becomes the same or smaller in every iteration of the loop.
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.Min(intervals[i][0], newInterval[0]);
            newInterval[1] = Math.Max(intervals[i][1], newInterval[1]);
            i += 1;
        }
        res.Add(newInterval);

        while (i < n) {
            res.Add(intervals[i]);
            i += 1;
        }

        return res.ToArray();
    }
}
