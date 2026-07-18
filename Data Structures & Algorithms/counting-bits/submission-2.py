class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            count = 0
            while num:
                count += 1 if num & 1 else 0
                num >>= 1
            res.append(count)
        return res