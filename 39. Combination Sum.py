class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(res:List[List[int]], curr:List[int], start:int):
           
            if sum(curr) == target:
                res.append(curr[:])
                return
            if sum(curr) > target:
                return
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                dfs(res, curr, i)
                curr.remove(candidates[i])
                
        res = []
        dfs(res, [], 0)
        return res
