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
        
# solution 3. morris
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node, output = root, []
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                precessor = node.left
                while precessor.right and precessor.right is not node:
                    precessor = precessor.right
                if not precessor.right:
                    output.append(node.val)
                    precessor.right = node
                    node = node.left
                else:
                    precessor.right=None
                    node = node.right
        return output
