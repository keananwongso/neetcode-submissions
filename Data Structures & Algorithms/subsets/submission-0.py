class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            # reached the leaf
            if i >= len(nums):
                res.append(subset.copy())
                return

            # we want to add the nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # we don't want to add nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
    