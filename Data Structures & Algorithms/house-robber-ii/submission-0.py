class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dp(i, end):
            if i >= end:
                return 0
            
            if (i, end) in memo:
                return memo[(i, end)]
            
            # rob
            rob = nums[i] + dp(i + 2, end)

            # skip
            skip = dp(i + 1, end)

            memo[(i, end)] = max(rob, skip)
            return memo[(i, end)]
        
        if len(nums) == 1:
            return nums[0]

        return max(dp(0, len(nums) - 1), dp(1, len(nums)))
    
    # T: O(n)
    # S: O(n)