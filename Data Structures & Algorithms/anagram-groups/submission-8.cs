public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        // dictionary. Keys string 0 - 25 representing the letters.
        var acum = new Dictionary<string, List<string>>();

        foreach (var str in strs) {
            var key = GetKey(str);
            if (acum.ContainsKey(key)) {
                acum[key].Add(str);
            } else {
                acum[key] = new List<string>() { str };
            }
        }

        return acum.Values.ToList<List<string>>();
    }

    public static string GetKey(string str) {
        int[] keyNums = new int[26];
        foreach (char c in str) {
            keyNums[c - 'a'] += 1; 
        }

        return string.Join(",", keyNums);
    }
}
