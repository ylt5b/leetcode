# solution 1: dfs

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res
    
    
    def dfs(self, root, result):
        if not root:
            return
        self.dfs(root.left, result)
        result.append(root.val)
        self.dfs(root.right, result
        
# solution 2: iterative soluiton
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res
           
  
