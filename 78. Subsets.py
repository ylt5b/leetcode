class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        def dfs(res:List[List[int]], cur:List[int], start):
            res.append(cur[:]) 
            for i in range(start, len(nums)):
                cur.append(nums[i])
                dfs(res, cur, i+1)
                cur.remove(nums[i])
                
                
        res = []
        dfs(res, [], 0)
        return res
