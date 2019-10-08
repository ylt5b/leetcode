class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        def dfs(index:int, path:str, res:List[str]):
            if index == len(digits):
                res.append(path)
                return
            for letter in map[int(digits[index])]:
                dfs(index + 1, path + letter, res)
        res = []
        if digits:
            dfs(0, '', res)
            return res
