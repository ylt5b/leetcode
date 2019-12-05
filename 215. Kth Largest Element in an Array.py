class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 1. quick select O(n)
        def partition(lo, hi, k):
            pivot = nums[lo]
            i = lo + 1
            j = hi 
            while i <= j:
                while i <= hi and nums[i] <= pivot: i += 1
                while j > lo and nums[j] >= pivot: j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
            nums[lo], nums[j] = nums[j], nums[lo]
            
            if k == j:
                return nums[j]
            elif j > k:
                partition(lo, j-1, k)
            else:
                partition(j+1, hi, k)
                
        partition(0, len(nums)-1, len(nums)-k)
        return nums[ -k]        
        
        
        # 2. heap  O(nlogk)
          heap = []

        
         for num in nums:
             if len(heap) < k:
                 heapq.heappush(heap, num)
             else:
                 heapq.heappushpop(heap, num)  
         return heapq.heappop(heap)
