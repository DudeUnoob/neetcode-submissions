class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        
        def dfs(r, c):

            if r >= ROWS or c >= COLS or r < 0 or c < 0:
                return

            if (r, c) in visited:
                return

            if grid[r][c] == "0":
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return






        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] != "1":
                    continue

                if (r, c) in visited:
                    continue
                
                res += 1
                dfs(r, c)

        return res