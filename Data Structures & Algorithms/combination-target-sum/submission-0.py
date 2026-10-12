class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        ssum = []

        def dfs(i, total):
            if total == target:
                res.append(ssum.copy())
                return

            if i >= len(nums) or total > target: 
                return
            
            # case that we want to take nums[i]
            ssum.append(nums[i])
            dfs(i, total + nums[i])

            # case that we DON't want to take nums[i]
            ssum.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
    
    # T: O(n * 2^t)
    # S: O(n + t)
        