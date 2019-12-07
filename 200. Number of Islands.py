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
  # bfs
        four_direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def isValid(self, i, j, grid):
            if 0 <= i <= len(grid)-1 and 0 <= j <= len(grid[0]) - 1:
                return True
            return False
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            grid[r][c] == '0'
            while queue:
                r, c = queue.popleft()
                for nr, nc in four_direction:
                    nr += r
                    nc += c
                    if isValid(self, nr, nc, grid) and grid[nr][nc] == '1':
                        queue.append((nr, nc))
                        grid[nr][nc] = '0'
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(i, j)
                    count += 1
        return count
  # union find

class DSU():
    def __init__(self, m, n, grid):
        self.parent = [0] * (m*n)
        self.rank = [0] * (m*n)
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.rank[i * n + j] = 1
                    self.count += 1
                else:
                    self.parent[i * n + j] = -1
                    self.rank[i * n + j] = 0

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
       
    def union(self, x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.rank[root_x] += self.rank[root_y]
            self.parent[root_y] = root_x
            self.count -= 1
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
            self.count -= 1
        print (self.count)
        return True
    
    def getCount(self):
        return self.count
    
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nr = len(grid)
        if nr == 0: return 0
        nc = len(grid[0])
        uf = DSU(nr, nc, grid)
        print (uf.parent)
        
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    if i-1>= 0 and grid[i-1][j] == '1':
                        uf.union((i-1)*nc+j, i* nc + j)
                    if j-1 >= 0 and grid[i][j-1] == '1':
                        uf.union(i * nc + j, i*nc+j-1)
                    if i+1 <= nr-1 and grid[i+1][j] == '1':
                        uf.union(i*nc + j, (i+1)*nc+j)
                    if j+1 <= nc-1 and grid[i][j+1] == '1':
                        uf.union(i*nc + j, i*nc + j+1)
        return uf.getCount()
        
   
