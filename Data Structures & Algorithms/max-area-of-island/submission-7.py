class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        visited = set()

        area = 0

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        
        def dfs(r, c):

            if (r, c) in visited:
                return 0

            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                grid[r][c] == 0):
                return 0

            visited.add((r, c))
            current_area = 1

            for nr, nc in directions:
                current_area += dfs(r + nr, c + nc)

            return current_area
            





        
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 1 and (r, c) not in visited:
                    
                    area = max(area, dfs(r, c))

        return area

        
