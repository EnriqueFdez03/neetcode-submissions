class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if c.isalnum()]
        l, r = 0, len(chars) - 1

        while l < r:
            if chars[l] != chars[r]:
                return False
            l += 1
            r -= 1
        
        return True