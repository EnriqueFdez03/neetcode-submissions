class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        
        columns = [set() for _ in range(N)]
        subBoxes = dict()
        for r in range(N):
            row = board[r]
            visited = set()
            for c in range(N):
                if row[c] == ".":
                    continue
                if row[c] in visited:
                    return False
                visited.add(row[c])
                
                if row[c] in columns[c]:
                    return False
                columns[c].add(row[c])

                boxPos = (r // 3, c // 3)
                if boxPos in subBoxes:
                    if row[c] in subBoxes[boxPos]:
                        return False
                    subBoxes[boxPos].add(row[c])
                else:
                    subBoxes[boxPos] = { row[c] }
        return True
