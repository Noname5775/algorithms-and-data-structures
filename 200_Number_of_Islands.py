class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # Проверка границ
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Если это не земля, прекращаем обход
            if grid[r][c] != "1":
                return

            # Помечаем клетку как посещённую
            grid[r][c] = "0"

            # Обходим соседей
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands