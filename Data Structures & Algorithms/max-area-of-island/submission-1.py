class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        count = 0

        visited = set()

        def dfs(r, c):

            nonlocal maxArea, count

            if (r >= ROWS or c >= COLS or r < 0 or c < 0):
                return

            if (r, c) in visited:
                return

            if grid[r][c] == 0:
                return

            
            visited.add((r, c))
            count += 1

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

            maxArea = max(count, maxArea)

            return maxArea

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 0:
                    continue
                count = 0
                dfs(r, c)


        return maxArea