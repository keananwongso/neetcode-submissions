# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # checks height of each root
        def dfs(curr):
            if curr is None:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            
            # check if child found imbalance
            if left == -1 or right == -1:
                return -1
            # current node imbalanced
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)

        return dfs(root) != -1
    
    # T: O(n)
    # S: O(h)