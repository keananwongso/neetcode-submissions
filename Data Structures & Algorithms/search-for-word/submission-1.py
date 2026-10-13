class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # base case 
            if i == len(word):
                return True

            # we want to return false
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or 
                (r, c) in path):
                return False

            # that means, board[r][c] == letter in word
            # continue recrusion
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False

        # T: O(m * n^4)
        # S: O(n)
