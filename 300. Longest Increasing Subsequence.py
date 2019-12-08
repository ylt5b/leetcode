class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
    # 1. dp O(n^2)
        if not nums: return 0
        
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            temp = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = max(temp, dp[j])
            dp[i] = temp + 1
        return max(dp)
    
    # 2. dp + binary search O(nlogn)
        if not nums: return 0
        tail = [nums[0]]
        size = 0
        for i in range(1, len(nums)):
            idx = bisect.bisect_left(tail, nums[i])
            if idx == len(tail):
                tail.append(nums[i])
            else:
                tail[idx] = nums[i]
        return len(tail)
