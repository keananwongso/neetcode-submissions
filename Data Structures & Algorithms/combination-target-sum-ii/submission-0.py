class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        ssum = []

        def dfs(i, total):
            if total == target:
                res.append(ssum.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            # case we take candidates[i]
            ssum.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            # case we dont take candidates[i]
            ssum.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res
    
    # T: O(n * 2^n)
    # S: O(n)