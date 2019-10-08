class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(res: List[List[int]], cur: List[int]):
            if len(cur) == len(nums): 
                res.append(cur[:])
                return
            for i in range(len(nums)):
                if nums[i] in cur:
                    continue
                cur.append(nums[i])
                dfs(res, cur)
                cur.remove(nums[i])
                
        res = []
        dfs(res, [])
        return res
      
