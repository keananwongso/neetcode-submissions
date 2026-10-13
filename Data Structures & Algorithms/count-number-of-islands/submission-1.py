class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        count = 0
        seen = set()

        def bfs(r, c):
            q = collections.deque([(r, c)])
            seen.add((r, c))

            while q:
                r, c = q.popleft()
                
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc  

                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == "0" or
                        (nr, nc) in seen):
                        continue
                    
                    seen.add((nr, nc))
                    q.append((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    count += 1
                
        return count
