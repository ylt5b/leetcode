class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(res:List[List[int]], cur:List[int], start:int):
            if sum(cur) == target:
                res.append(cur[:])
                return
            if sum(cur) > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                dfs(res, cur, i + 1)
                cur.remove(candidates[i])
                
        res = []
        candidates.sort()
        dfs(res, [], 0)
        return res
