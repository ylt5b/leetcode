# solution 1: dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
                     
        def withRange(i:int, j:int) -> bool:
            if i >= 0 and j >= 0 and i<= len(grid) - 1 and j <= len(grid[0]) - 1:
                return True
            return False
    
        def dfs(i:int, j:int) ->None:
            for (x, y) in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if withRange(x, y) and grid[x][y] == '1':
                    print (x, y)
                    grid[x][y] = '0'
                    dfs(x, y)
        
        
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        visited = [[0] * n for _ in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    dfs(i,j)
                    
        return result
        
   
