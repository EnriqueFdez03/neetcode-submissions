class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # reminds me to combination sum + isPalindrome. Do we need two
        # pointers for the is palindrome? any smarter way?
        res = []
        path = []

        def backtrack(i):  # sliding window approach
            if i >= len(s):
                res.append(path.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j + 1]):
                    path.append(s[i:j + 1])
                    backtrack(j + 1)
                    path.pop()
            
        backtrack(0)
        return res

    def isPalindrome(self, word):
            if len(word) == 0:
                return False # to avoid adding []

            l, r = 0, len(word) - 1

            while l <= r:
                if word[l] != word[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True


