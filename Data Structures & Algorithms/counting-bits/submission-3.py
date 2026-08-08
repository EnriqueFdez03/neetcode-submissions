class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(0, n + 1):
            ones = 0
            for i in range(32):
                if (1 << i) & num:
                    ones += 1
            res.append(ones)

        return res