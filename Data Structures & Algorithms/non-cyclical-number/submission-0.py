class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        sol = False
        while not False:
            digits = self.getDigits(n)
            print(digits)
            curr = sum(v**2 for v in digits)
            if curr in results:
                break
            results.add(curr)
            sol = curr == 1
            n = curr
        return sol


    def getDigits(self, n):
        digits = []
        while n > 0:
            digits.append(n % 10)
            n = n // 10
        return digits