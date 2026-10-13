class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        seen = set()
        max_area = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0 or 
                (r, c) in seen):
                return 0
            
            seen.add((r, c))
            area = 1

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                area += dfs(r + dr, c + dc)
            return area

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    max_area = max(max_area, dfs(r, c))

        return max_area
        
    # T: O(m * n)
    # S: O(m * n)