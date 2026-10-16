class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # base cases

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[n - 1]

        # n = len(nums)
        # dp = [0] * (n + 2)

        # for i in range(n - 1, -1, -1):
        #     dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        
        # return dp[0] 
    
    # T: O(n)
    # S: O(n)