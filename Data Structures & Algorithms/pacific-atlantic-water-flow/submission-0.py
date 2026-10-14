class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevHeight):
            # base case: already visited
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or heights[r][c] < prevHeight
                or (r, c) in visited):
                return
            
            visited.add((r, c))

            # explore 4 neighbors
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                dfs(nr, nc, visited, heights[r][c])
                
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            for c in range(COLS):
                # if heights[r][c] reaches BOTH pacific & atlantic, return TRUE
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
            
        return res  

    # T: O(m * n)
    # S: O(m * n)