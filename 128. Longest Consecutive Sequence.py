class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
            
        def union(x, y):
            x_parent = find(x)
            y_parent = find(y)
            if x_parent == y_parent:
                return True
            if size[x_parent] > size[y_parent]:
                parent[y_parent] = x_parent
                size[x_parent] += size[y_parent]
            else:
                parent[x_parent] = y_parent
                size[y_parent] += size[x_parent]
                
        if not nums:
            return 0
        hashtable = {}
        
        parent = [i for i in range(len(nums))]
        size = [1] * len(nums)
        for i in range(len(nums)):
            if nums[i] in hashtable:
                continue
            hashtable[nums[i]] = i
            if nums[i] - 1 in hashtable:
                union(i, hashtable[nums[i] - 1 ])
            if nums[i] + 1 in hashtable:
                union(i, hashtable[nums[i] + 1 ])
                
        return max(size)
