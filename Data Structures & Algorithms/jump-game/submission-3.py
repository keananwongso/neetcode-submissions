class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False # means we were stuck in prev
            
            farthest = max(farthest, i + nums[i])

            # check if arldy reached goal (end)
            if farthest >= len(nums) - 1:
                return True
        return True

    # T: O(n)
    # S: O(1)