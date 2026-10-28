class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647

        q = deque()

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == 0:
                    q.append((r, c))

        

        while q:

            r, c = q.popleft()

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c


                if nr < 0 or nr >= ROWS or nc <0 or nc >= COLS:
                    continue

                if grid[nr][nc] != INF:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1

                q.append((nr, nc))
