class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        acum = set()
        for num in nums:
            if num in acum:
                return True
            else:
                acum.add(num)
        return False