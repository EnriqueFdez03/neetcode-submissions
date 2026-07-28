class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # play with a stack
        # position and speed, reverse sort based on position
        posAndSpeed = [(p, s) for p, s in zip(position, speed)]
        posAndSpeed.sort(reverse=True)

        stack = []
        for (p, s) in posAndSpeed:
            timeToReach = (target - p) / s
            if not stack:
                stack.append(timeToReach)
            else:
                nextCarTime = stack[-1]
                if timeToReach > nextCarTime:
                    stack.append(timeToReach)
        
        return len(stack)