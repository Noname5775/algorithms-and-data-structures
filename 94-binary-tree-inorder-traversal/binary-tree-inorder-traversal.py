# Обход: Left -> Root -> Right
class Solution:
    def inorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)        # идем в левое поддерево
            result.append(node.val)  # посещаем узел
            dfs(node.right)       # идем в правое поддерево

        dfs(root)
        return result