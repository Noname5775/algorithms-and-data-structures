class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)

        # если меньше — идем влево
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            # иначе вправо
            root.right = self.insertIntoBST(root.right, val)

        return root