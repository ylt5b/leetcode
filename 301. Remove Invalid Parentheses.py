class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # minimal number to remove
       
        
        left, right = 0, 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0 :
                    left -= 1
                else:
                    right += 1
        
        def dfs(index, path, left, right, extra):
            if path in res: return 
            if index == len(s):
                if left == 0 and right == 0:
                    res.append(path)
                return 
            # Discard case
            if s[index] == '(' and left > 0:
                dfs(index + 1, path, left - 1, right, extra)
            if s[index] == ')' and right > 0:
                dfs(index + 1, path, left, right-1, extra)
                
            # Keep case
            if s[index] not in '()':
                dfs(index + 1, path + s[index], left, right, extra)
            elif s[index] == '(':
                dfs(index + 1, path + s[index], left, right, extra+1)
            elif s[index] == ')' and extra > 0 :
                dfs(index + 1, path + s[index], left, right, extra-1)
                
        res = []
        dfs(0, '', left, right, 0)
        return res
            
