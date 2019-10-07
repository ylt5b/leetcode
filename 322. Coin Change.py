# Solution 1. DP with bottom up
    # 1. coins outer loop
    class Solution(object):
        def coinChange(self, coins, amount):
            dp = [0] + [float('inf')] * amount
            for coin in coins:
                for i in range(coin, amount+1):
                    dp[i] = min(dp[i], dp[i-coin] + 1)
            return dp[-1] if dp[-1] != float('inf') else -1
        
     # 2. amount outer loop
     class Solution(object):
        def coinChange(self, coins, amount):
            dp = [0] + [float('inf')] * amount
            for i in range(1, amount + 1):
                for coin in coins:
                    if i - coin >= 0:
                        dp[i] = min(dp[i], dp[i-coin] + 1)
            return dp[-1] if dp[-1] != float('inf') else -1
    
