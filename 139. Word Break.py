# Solution 1: DP
class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i+1, len(s)+1):
                    if s[i:j] in wordDict:
                        dp[j] = True
        return dp[-1]

 # Solution 2: BFS
class Solution(object):
    def wordBreak(self, s, wordDict):
        stack = [0]
        visited = set()
        while stack:
            start = stack.pop()
            if start in visited:
                continue
            visited.add(start)
            for word in wordDict:
                if s[start:].startswith(word):
                    if len(word) == len(s[start:]):
                        return True
                    stack.append(start + len(word))
        return False
    
  # Solution 3: DFS
class Solution(object):
    def wordBreak(self, s, wordDict):
            def dfs(index, visit):
            if index == len(s):
                return True
            if visit[index] == True:
                return 
            visit[index] = True
            for j in range(index + 1, len(s) + 1):
                if s[index:j] in wordDict and dfs(j, visit):
                    return True
            return False
      
        visit = [False] * (len(s) + 1)
        return dfs(0, visit)

    # DFS with memoization:
    class Solution:
        def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
         def dfs(start:int, visited, memo):
            if start == len(s):
                return True
            if memo[start] != None:
                return memo[start]
            if start in visited: 
                return
            visited.add(start)
            for i in range(start+1, len(s)+1):
                if s[start:i] in wordDict and dfs(i, visited, memo):
                    memo[start] = True
                    return memo[start]
                
            memo[start] = False
            return memo[start] 
        
         visited = set()
         memo = [None] * len(s)
         return dfs(0, visited, memo)
