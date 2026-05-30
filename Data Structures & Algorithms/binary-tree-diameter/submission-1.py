# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # solution using iterative dfs + memoization 
        # to calculate diameter of a node I need:
        #   - left height
        #   - right height, BC -> d(root) = leftH (inc. self) + rightH (inc. self)
        # to calculate the height of a node I need the height of the previous
        # ones. to calculate the diameter of a node I also need the diameter of the 
        # previous ones, so that res relies in the max diameter.
        # iterative dfs -> stack + pop()
        stack = [root]
        mp = {None:(0, 0)} # height, diameter for node mp[key]

        while stack:
            # if we have childs add them (dfs), if don't, pop and calculate heights and diameter
            node = stack[-1]

            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                curr = stack.pop()

                leftH, leftD = mp[curr.left]
                rightH, rightD = mp[curr.right]

                mp[curr] = (1 + max(leftH, rightH), 
                    max(leftH + rightH, leftD, rightD))
            
        return mp[curr][1]


