Soluiton 1: iterative

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res
        
Solution 2: recursive

class Solution:
  def preorderTraversal(self, root: TreeNode) -> List[int]:
      res = []
      self.dfs(root, res)
      return res

  def dfs(self, root, res):
      if not root:
          return
      res.append(root.val)
      self.dfs(root.left, res)
      self.dfs(root.right, res)
