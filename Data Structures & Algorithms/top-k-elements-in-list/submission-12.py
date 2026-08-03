from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        for num, reps in counter.items():
            buckets[reps].append(num)
        
        res = []
        for bucket in buckets[::-1]:
            while bucket:
                if k == 0:
                    break
                res.append(bucket.pop())
                k -= 1
        
        return res