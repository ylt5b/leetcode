class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
  #1. divide and conquer
        def cross_sum(left, right, p):
            if left == right:
                return nums[left]
            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left-1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)
                
            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p+1, right+1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)
            return left_subsum +  right_subsum          
                
                
                
        def helper(left, right):
            if left == right: return nums[left]
            p = (left + right) // 2
            left_sum = helper(left, p)
            right_sum = helper(p+1, right)
            cross_summ = cross_sum(left, right, p)
            
            return max(left_sum, right_sum, cross_summ)
        
        return helper(0, len(nums)-1)
        
   # 2. dp
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)

          curr_sum = nums[0]
        global_sum = curr_sum
     
        for i in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[i], nums[i])
            global_sum = max(curr_sum, global_sum)
        return global_sum
