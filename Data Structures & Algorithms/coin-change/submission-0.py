class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(i, remaining):
            # successfully found
            if remaining == 0:
                return 0
            
            # invalid
            if i >= len(coins) or remaining < 0:
                return float('inf')

            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            # choice 1: use current coin
            take = 1 + dp(i, remaining - coins[i])

            # choice 2: skip current coin
            skip = dp(i + 1, remaining)

            memo[(i, remaining)] = min(take, skip)
            return memo[(i, remaining)]

        res = dp(0, amount)
        return res if res != float('inf') else -1

        # T: O(nA)
        # S: O(nA)