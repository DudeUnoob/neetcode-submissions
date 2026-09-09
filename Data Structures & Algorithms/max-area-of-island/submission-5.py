class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        max_area = 0

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):

            nonlocal area
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            if (r, c) in visited:
                return

            if grid[r][c] == 0:
                return

            

            
            visited.add((r, c))
            area += 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
            



        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 0 or (r, c) in visited:
                    continue

                area = 0
                dfs(r, c)

                max_area = max(max_area, area)

        return max_area



        