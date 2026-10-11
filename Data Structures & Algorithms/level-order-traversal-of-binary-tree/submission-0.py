# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        if root is None:
            return []

        q = deque([root]) 

        while q:
            local_array = []
            for i in range(len(q)):
                node = q.popleft()
                local_array.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            self.res.append(local_array)

        return self.res

    # T: O(n)
    # S: O(w)