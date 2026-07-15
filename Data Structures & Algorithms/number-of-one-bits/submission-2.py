class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n: # while not 0
            res += 1 if n & 1 else 0 # si el último bit es uno
            n >>= 1 # desplaza un bit a la derecha
        return res