from collections import Counter

class Solution:
    # now using bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        reps = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for n, rep in reps.items():
            bucket[rep].append(n)

        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                if len(result) < k:
                    result.append(num)

        return result