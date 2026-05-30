class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(pos, speed) for pos, speed in sorted(zip(position, speed), key=lambda x: x[0], reverse=True)]
        
        stack = []
        
        for p, s in pair:
            arrivalTime = (target - p) / s
            if not stack or stack[-1] < arrivalTime:
                stack.append(arrivalTime)
                print(stack)

        return len(stack)

        
        