class Solution:
    def isHappy(self, n: int) -> bool:
        # if there´s a cycle we reach a loop
        slow, fast = n, self.sumOfSquares(n)
        while slow != fast:
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            slow = self.sumOfSquares(slow)
        return fast == 1


    def sumOfSquares(self, n):
        output = 0
        while n > 0:
            output += (n % 10) ** 2
            n = n // 10
        return output