class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = 0
        right = 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        print (left, right)       
        def dfs(index, curr, left, right, res, leftextra):
            if index == len(s):
                if left == 0 and  right == 0: 
                    possible = ''.join(curr)
                    if possible not in res:
                        res.append(possible)
                return
            
            if s[index] == '(' and left > 0:
                dfs(index + 1, curr, left -1, right, res, leftextra)
            elif s[index] == ')' and right > 0:
                dfs(index + 1, curr, left, right -1, res, leftextra)
                
            curr.append(s[index])
            if s[index] not in '()':
                dfs(index + 1, curr, left, right, res, leftextra)      
            elif s[index] == '(' :
                dfs(index + 1, curr, left, right, res, leftextra+1)
            elif s[index] == ')' and leftextra > 0:
                dfs(index + 1, curr, left, right, res, leftextra -1)
            curr.pop()
            
        res = []
        dfs(0, [] , left, right, res, 0)
        return list(res)
