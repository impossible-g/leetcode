# _*_coding:utf-8_*_
# __author: a123456
from utils.utils import TreeNode, generate_tree_node


class Solution:
    """
    前序遍历
    """

    def preorderTraversal(self, root: TreeNode) -> [int]:
        # 递归法
        if not root:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal(self, root: TreeNode) -> [int]:
        # 迭代法
        stack = []
        result = []

        while root or stack:
            while root:
                stack.append(root)
                result.append(root.val)
                root = root.left

            if stack:
                root = stack.pop()
                root = root.right
        return result



if __name__ == '__main__':
    s = Solution()
    t = [1, None, 2, 3]
    tree = generate_tree_node(t)
    print(s.preorderTraversal(tree))
