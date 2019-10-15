# solution 1: iterative

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]
        
# solution 2: dfs
 class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res
        
        
    def dfs(self, root, res):
        if not root:
            return 
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)
