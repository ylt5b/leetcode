class Solution(object):
    def generateParenthesis(self, n):
        def dfs(path,res, left, right):
                if right > left:
                    return
                if right > n or left > n:
                    return
                if len(path) == 2*n:
                    res.append(path)
                    return
                dfs(path + '(', res, left + 1, right)
                dfs(path + ')', res, left, right + 1)
        
        res = []
        if n == 0:
            return ''
        else:
            dfs('', res, 0, 0)
            return res
