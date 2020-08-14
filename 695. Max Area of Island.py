# solution: dfs
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            res = 0
            for (new_i, new_j) in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                res += dfs(new_i, new_j)
            return res + 1
                
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
                    
        return res
        
 # time Complexity: O(m*n)
 # space Complexity: O(m*n)
