class Solution(object):
    def getMaximumGold(self, grid):
        def dfs(i, j, seen):
            seen[i][j] = 1 
            mx = 0
            for (x, y) in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if x >= 0 and y >= 0 and x <= len(grid)-1 and y <= len(grid[0]) - 1 and seen[x][y] == 0 and grid[x][y] != 0:
                    mx = max(grid[x][y] + dfs(x, y, seen), mx)
            seen[i][j] = 0
            return mx
        
        
        m = len(grid)
        n = len(grid[0])
        seen = [[0] * n for _ in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    result = max(result, grid[i][j] + dfs(i, j, seen))
                    
        return result
