# union find
class DSU():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] > self.rank[root_y]:
            self.rank[root_x] += self.rank[root_y]
            self.parent[root_y] = root_x
            self.rank[root_y] = 0
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
            self.rank[root_x] = 0
        return True
    
    
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """ 
        dsu = DSU(len(stones))
        for i in range(len(stones)):
            for j in range(i, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                   dsu.union(i, j)
          
        max_move = 0
        for i in range(len(stones)):
            if dsu.rank[i] > 1:
                max_move += dsu.rank[i] - 1
        return max_move
