class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_so_far=prices[0]
        best_result=0

        for i in range(len(prices)):
            best_result = max(best_result, prices[i] - min_so_far)

            if prices[i] < min_so_far:
                min_so_far = prices[i]

        return best_result
            

# T: O(n)
# S: O(1)

