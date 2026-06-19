import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        if len(s) < 1:
            return s
        if len(s) == 2:
            return "" if s[0] == s[1] else s
        
        longest = 0
        countDict = {}
        for c in s:
            countDict[c] = countDict.get(c, 0) + 1
            longest = max(longest, countDict[c])
        if longest > (len(s) + 1) // 2:
            return ""
        
        heap = []
        for c, rep in countDict.items():
            heapq.heappush(heap, (-rep, c))
        
        sol = []
        carry = None
        while heap:
            freq, c = heapq.heappop(heap)
            freq = -freq

            if carry:
                heapq.heappush(heap, carry)
                carry = None

            sol.append(c)
            freq -= 1
            if freq != 0:
                carry = (-freq, c)

        return "".join(sol)


