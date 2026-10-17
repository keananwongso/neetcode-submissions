class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            cur = intervals[i]
            prev = res[-1]

            # cond when there is overlap
            if prev[1] >= cur[0]:
                prev[1] = max(prev[1], cur[1])
            else:
                res.append(cur)

        return res
    
    # T: O(n lgn)
    # S: O(n)
            