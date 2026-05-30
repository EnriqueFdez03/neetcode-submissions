class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # let´s go with the greedy.
        '''
        start from the last index and mark it as goal.
        see if from any index we can reach to that goal.
        if so, change goal. Keep going back. If we reach
        position 0 return True else False
        '''
        if len(nums) == 1:
            return True

        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        return goal == 0