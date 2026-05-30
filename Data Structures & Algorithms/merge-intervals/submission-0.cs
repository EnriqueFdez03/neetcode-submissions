public class Solution {
    public int[][] Merge(int[][] intervals) {
        Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));
        var result = new List<int[]>() { intervals[0] };
        
        foreach (int[] interval in intervals) {
            var start = interval[0];
            var end = interval[1];
            var lastEnd = result[result.Count - 1][1];
            if (start <= lastEnd) {
                result[result.Count - 1][1] = Math.Max(lastEnd, end);
            } else {
                result.Add(interval);
            }
        }

        return result.ToArray();
        
    }
}
