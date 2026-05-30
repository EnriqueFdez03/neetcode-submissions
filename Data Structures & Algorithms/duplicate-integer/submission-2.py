class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        acum = set()
        for n in nums:
            if n in acum:
                return True
            acum.add(n)
        
        return False