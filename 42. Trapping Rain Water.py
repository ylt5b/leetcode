class Solution:
    def trap(self, height: List[int]) -> int:
        # stack
         stack = []
         res = 0
         for i in range(len(height)):
             while stack and height[i] > height[stack[-1]]:
                 t = stack.pop()
                 if not stack: continue
                 res += (min(height[i], height[stack[-1]]) - height[t]) * (i - stack[-1] - 1)
             stack.append(i)
           
         return res
         
     # two pointer

        if len(height) < 3:
            return 0
        l, r = 0, len(height) - 1
        left_max = height[l]
        right_max = height[r]
        res = 0
        while l < r:
            right_max = max(right_max, height[r])
            left_max = max(left_max, height[l])      
            if left_max < right_max:
                res += left_max - height[l]
                l += 1
            else:
                res += right_max - height[r]
                r -= 1
        return res
        
        
     # dynamic programming
      if not height: return 0
      left = [0] * len(height)
      right = [0] * len(height)
      left[0] = height[0]
      right[-1] = height[-1]
      for i in range(1, len(height)):
          left[i] = max(left[i-1], height[i])

      for j in range(len(height)-2, -1, -1):
          right[j] = max(right[j+1], height[j])
      res = 0 
      for i in range(len(height)):
          res += min(left[i], right[i]) - height[i]

      return res
