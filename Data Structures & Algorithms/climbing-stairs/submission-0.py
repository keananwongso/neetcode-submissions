class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(i):
            # base cases
            if i == 2:
                return 2
            
            if i == 1:
                return 1

            # already computed
            if i in memo:
                return memo[i]
            
            # recurrence 
            memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]

        return dp(n)

    # T: O(n)
    # S: O(n)