class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            count = 0
            for i in range(32):
                count += 1 if num & 1 else 0
                num >>= 1
                if not num:
                    break
            res.append(count)
        return res