class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            fuel = gas[i] - cost[i]
            if fuel < 0:
                continue

            j = (i + 1) % n
            while j != i:
                fuel = fuel - cost[j] + gas[j]
                if fuel < 0:
                    break
                j += 1
                j = j % n

            if j == i:
                return i
        return -1