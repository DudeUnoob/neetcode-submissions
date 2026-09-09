class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0


        def dfs(r, c):
                
            if (r, c) in visited:
                return

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
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

                if grid[r][c] == "0" or (r, c) in visited:
                    continue
                islands += 1
                dfs(r, c)



        return islands