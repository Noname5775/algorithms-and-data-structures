# Обход: Left -> Right -> Root
class Solution:
    def postorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)  # в конце узел

        dfs(root)
        return result