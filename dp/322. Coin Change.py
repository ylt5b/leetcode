class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * amount
        #solution 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
                
        # solution 2
#         for i in range(1, amount + 1):
#             for coin in coins:
#                 if i - coin >= 0:
#                     dp[i] = min(dp[i], dp[i-coin] + 1)
      
        return dp[-1] if dp[-1] != float('inf') else -1
    
