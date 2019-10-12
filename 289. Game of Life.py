# soluiton 1: bit manipulation

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def neighbour(i, j):
            total = 0
            for x,y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1), (i-1, j-1), (i-1, j+1), (i+1, j+1), (i+1, j-1)):
                if x >= 0 and y >= 0 and x <= len(board) -1 and y <= len(board[0]) -1 and board[x][y] & 1:
                    total += 1
            return total
        
        def rule(value,i, j):
            if value == 1:
                if neighbour(i, j) == 2 or neighbour(i, j) == 3:
                    value |= 2
            elif value == 0:
                if neighbour(i, j) == 3:
                    value |= 2
            return value
                    
        if not len(board):
            return []
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):       
                board[i][j] = rule(board[i][j], i, j) 
                
        for i in range(m):
            for j in range(n):       
                board[i][j] = board[i][j] >> 1 
                
       
                
        return board
