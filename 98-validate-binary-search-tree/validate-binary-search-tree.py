# Проверяем, что дерево удовлетворяет свойствам BST
class Solution:
    def isValidBST(self, root):

        def dfs(node, low, high):
            if not node:
                return True
            
            # значение должно быть в диапазоне
            if not (low < node.val < high):
                return False

            # проверяем левое и правое поддерево
            return (dfs(node.left, low, node.val) and
                    dfs(node.right, node.val, high))

        return dfs(root, float('-inf'), float('inf'))