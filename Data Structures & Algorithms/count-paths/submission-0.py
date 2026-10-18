class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def dp(r, c):
            # out of bounds
            if r >= m or c >= n:
                return 0

            # reached destination
            if r == m - 1 and c == n - 1:
                return 1
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r, c)] = dp(r + 1, c) + dp(r, c + 1)
            return memo[r, c]
        
        return dp(0, 0)

        # T: O(mn)
        # S: O(mn)