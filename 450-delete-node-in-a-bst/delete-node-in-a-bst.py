class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None

        # ищем узел
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # нашли узел

            # случай 1: нет левого ребенка
            if not root.left:
                return root.right

            # случай 2: нет правого ребенка
            if not root.right:
                return root.left

            # случай 3: есть оба ребенка
            # находим минимальный в правом поддереве
            min_node = self.getMin(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)

        return root

    def getMin(self, node):
        while node.left:
            node = node.left
        return node