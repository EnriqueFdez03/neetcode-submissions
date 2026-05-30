class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            num = digits[i] + 1
            if num > 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else:
                digits[i] = num
                break
        return digits