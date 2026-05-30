from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, reps in freq.items():
            buckets[reps].append(num)
        
        sol = []
        for i in range(len(buckets) - 1, 0, -1):
            bucket = buckets[i]
            j = 0
            while len(sol) < k and j < len(bucket):
                sol.append(bucket[j])
                j += 1
                    
        return sol