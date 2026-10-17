class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        best = float('-inf')

        for i in range(len(nums)):
            cur = cur + nums[i]
            best = max(best, cur)

            if cur < 0:
                cur = 0
        
        return best

        # T: O(n)
        # S: O(1)