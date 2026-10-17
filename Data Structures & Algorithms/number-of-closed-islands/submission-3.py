class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        s = [] #stack

        def dfs(r, c):
            s.append((r, c))
            visited.add((r, c))
            closed = True
            
            while s:
                row, col = s.pop()

                for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nr, nc = row + dr, col + dc

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                        closed = False
                        continue
                    
                    if grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue

                    visited.add((nr, nc))
                    s.append((nr, nc))
            return closed

        count = 0
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and (r, c) not in visited:
                    if dfs(r, c):
                        count += 1
        return count
                   