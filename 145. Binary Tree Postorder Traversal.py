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

# solution 3: morris
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        node, res = root, []
        while node:
            if not node.right:
                res.append(node.val)
                node = node.left
            else:
                precessor = node.right
                while precessor.left and precessor.left != node:
                    precessor = precessor.left
                if not precessor.left:
                    res.append(node.val)
                    precessor.left = node
                    node = node.right
                else:
                    # precessor.left = None
                    node = node.left
                    
        return res[::-1]
