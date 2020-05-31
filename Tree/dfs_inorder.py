class TreeNode:
    def __init__(self, val=0, left=None, right=Node):
        super().__init__()
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root):
            return inorder(root.left)+[root.val]+inorder(root.right) if root else []

        return inorder(root)[k-1]

    def kthSmallest2(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root.val)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
