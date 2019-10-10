class Solution(object):
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return 
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
            
            
    # another solution
    
   class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
           
        def dfs(res:List[List[int]], index, cur_res:List[List[int]], seen:set()):
            if len(cur_res) == len(nums):
                res.append(cur_res[:])
                return
           
            for i in range(len(nums)):
                if i in seen: continue 
                if i > 0 and  i-1  in seen and nums[i] == nums[i-1]: continue  
                seen.add(i)
                print (seen)
                dfs(res, i, cur_res + [nums[i]], seen)
                seen.remove(i)
               
        res = []
        seen = set()
        nums.sort()
        dfs(res, 0, [], seen)
        return (res)
            
