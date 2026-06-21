class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) <= 1:
            return asteroids
        
        stack = []        
        for asteroid in asteroids:
            toAdd = True

            while toAdd and asteroid < 0 and stack and stack[-1] > 0:
                top = stack[-1]

                if top < abs(asteroid): # top explodes
                    stack.pop()
                elif top + asteroid == 0: # both explodes
                    stack.pop()
                    toAdd = False
                else:                     # incoming explodes
                    toAdd = False
            
            if toAdd:
                stack.append(asteroid)
            
        return stack