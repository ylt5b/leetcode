class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl',
                  'mno', 'pqrs', 'tuv', 'wxyz']
        
        def dfs(path, res, i):
            if i == len(digits):
                res.append(path)
                return
            for digit in mapping[int(digits[i])]:
                dfs(path + digit, res, i + 1)
        
        res = []
        if not digits:
                return []
        else:
            dfs('', res, 0)
            return res
