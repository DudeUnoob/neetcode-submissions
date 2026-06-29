class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = 0
        count = 0

        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        
        def dfs(r, c):
            nonlocal res, count

            if (r, c) in visited:
                return

            if r >= ROWS or c >= COLS or r < 0 or c < 0:
                return

            if grid[r][c] == 0:
                return


            visited.add((r, c))
            count += 1
            
            dfs(r + 1, c)
            dfs(r - 1 , c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            res = max(count, res)

            return res

        



        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 0:
                    continue

                if (r, c) in visited:
                    continue

                count = 0
                dfs(r, c)

        return res