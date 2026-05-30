class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # let´s do it following the Kahn + BFS algo
        adjList = { c: set() for w in words for c in w}
        indegree = { c: 0 for w in words for c in w}

        visitedEdges = set()
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if (w1[j], w2[j]) not in visitedEdges:
                        adjList[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                        visitedEdges.add((w1[j], w2[j]))
                    break
        
        # we got the graph, now proceed with the Kahn algo
        # BFS but first, add the nodes with no requisites
        queue = deque()
        for c in adjList.keys():
            if indegree[c] == 0:
                queue.append(c)
            
        # process the queue. FIRST those with indegree 0
        res = []
        while queue:
            char = queue.popleft()
            res.append(char)
            
            for nei in adjList[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        if len(res) != len(adjList):
            return ""
        
        return "".join(res)